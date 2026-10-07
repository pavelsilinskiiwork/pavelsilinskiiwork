#!/usr/bin/env python3
"""Refresh the auto-generated blocks of the profile README.

Blocks (each is optional; a block is skipped if its markers are missing):
  <!--REPOS:START-->    ... <!--REPOS:END-->      all public repositories (GitHub API)
  <!--WPPLUGINS:START--> ... <!--WPPLUGINS:END--> WordPress.org plugins (WP_USERNAME)
  <!--LEETCODE:START--> ... <!--LEETCODE:END-->   LeetCode stats (needs a username)

Standard library only.

Usage:
    GITHUB_USER=pavelsilinskiiwork python scripts/update_readme.py
    python scripts/update_readme.py --github-user NAME --leetcode-user NAME --no-forks
"""
import argparse
import html
import json
import os
import re
import sys
import urllib.request

# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #


def replace_block(text: str, name: str, body: str) -> str:
    start, end = f"<!--{name}:START-->", f"<!--{name}:END-->"
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if not pattern.search(text):
        raise KeyError(f"markers {start} / {end} not found in README")
    return pattern.sub(lambda _m: f"{start}\n{body}\n{end}", text)


def http_json(url: str, headers: dict, data: bytes | None = None):
    req = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


# --------------------------------------------------------------------------- #
# GitHub repositories
# --------------------------------------------------------------------------- #


def fetch_repos(user: str, token: str | None) -> list[dict]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "profile-readme-updater",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    repos, page = [], 1
    while True:
        url = (f"https://api.github.com/users/{user}/repos"
               f"?per_page=100&page={page}&type=owner&sort=pushed")
        chunk = http_json(url, headers)
        repos.extend(chunk)
        if len(chunk) < 100:
            return repos
        page += 1


def build_repos_block(repos: list[dict], user: str, include_forks: bool,
                      exclude: set[str]) -> str:
    rows = []
    for r in sorted(repos, key=lambda x: x.get("pushed_at") or "", reverse=True):
        if r["name"].lower() in exclude or r["name"].lower() == user.lower():
            continue  # skip the profile repo itself and anything excluded
        if r.get("archived"):
            continue
        if r.get("fork") and not include_forks:
            continue
        desc = (r.get("description") or "").strip() or "_No description yet_"
        meta = []
        if r.get("language"):
            meta.append(f"`{r['language']}`")
        if r.get("stargazers_count"):
            meta.append(f"⭐ {r['stargazers_count']}")
        if r.get("fork"):
            meta.append("fork")
        suffix = f" · {' · '.join(meta)}" if meta else ""
        rows.append(f"- [**{r['name']}**]({r['html_url']}) — {desc}{suffix}")
    return "\n".join(rows) if rows else "_No public repositories yet._"


# --------------------------------------------------------------------------- #
# WordPress.org plugins
# --------------------------------------------------------------------------- #


def fetch_plugins(wp_user: str) -> list[dict]:
    """Plugins authored by a WordPress.org username (official public API)."""
    from urllib.parse import urlencode
    qs = urlencode({
        "action": "query_plugins",
        "request[author]": wp_user,
        "request[per_page]": 100,
        "request[fields][short_description]": 1,
        "request[fields][active_installs]": 1,
        "request[fields][rating]": 1,
        "request[fields][num_ratings]": 1,
        "request[fields][last_updated]": 1,
    })
    data = http_json(f"https://api.wordpress.org/plugins/info/1.2/?{qs}",
                     {"User-Agent": "profile-readme-updater"})
    return data.get("plugins") or []


def _installs(n: int) -> str:
    if n >= 1000:
        return f"{n // 1000}k+" if n % 1000 == 0 or n >= 10000 else f"{n / 1000:.1f}k+"
    return f"{n}+" if n else "<10"


def build_plugins_block(plugins: list[dict]) -> str:
    if not plugins:
        return "_No plugins published yet._"
    rows = []
    for p in sorted(plugins, key=lambda x: x.get("active_installs") or 0, reverse=True):
        slug = p.get("slug", "")
        name = html.unescape(re.sub(r"<[^>]+>", "", p.get("name", slug))).strip()
        desc = html.unescape(re.sub(r"<[^>]+>", "", p.get("short_description") or "")).strip()
        meta = [f"{_installs(p.get('active_installs') or 0)} active installs"]
        if p.get("num_ratings"):
            meta.append(f"⭐ {round((p.get('rating') or 0) / 20, 1)}/5 ({p['num_ratings']})")
        line = f"- [**{name}**](https://wordpress.org/plugins/{slug}/)"
        if desc:
            line += f" — {desc}"
        rows.append(f"{line} · {' · '.join(meta)}")
    return "\n".join(rows)


# --------------------------------------------------------------------------- #
# LeetCode
# --------------------------------------------------------------------------- #

LEETCODE_QUERY = """
query userStats($username: String!) {
  matchedUser(username: $username) {
    submitStatsGlobal { acSubmissionNum { difficulty count } }
    userCalendar { streak totalActiveDays }
  }
}
"""


def build_leetcode_block(username: str, badge: str) -> str:
    payload = json.dumps({"query": LEETCODE_QUERY,
                          "variables": {"username": username}}).encode()
    data = http_json(
        "https://leetcode.com/graphql",
        {"Content-Type": "application/json",
         "Referer": f"https://leetcode.com/u/{username}/",
         "User-Agent": "Mozilla/5.0 (profile-readme-updater)"},
        payload,
    )
    user = (data.get("data") or {}).get("matchedUser")
    if not user:
        raise RuntimeError(f"LeetCode user '{username}' not found: {data.get('errors')}")
    solved = {r["difficulty"]: r["count"]
              for r in user["submitStatsGlobal"]["acSubmissionNum"]}
    cal = user["userCalendar"]
    lines = [
        f"- ✅ {solved.get('Easy', 0)} Easy · {solved.get('Medium', 0)} Medium · {solved.get('Hard', 0)} Hard",
        f"- 🔥 Current streak: {cal['streak']} days · {cal['totalActiveDays']} active days",
    ]
    if badge:
        lines.append(f"- 🏅 {badge}")
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--readme", default="README.md")
    ap.add_argument("--github-user",
                    default=os.environ.get("GITHUB_USER") or os.environ.get("GITHUB_REPOSITORY_OWNER"))
    ap.add_argument("--leetcode-user", default=os.environ.get("LEETCODE_USERNAME"))
    ap.add_argument("--wp-user", default=os.environ.get("WP_USERNAME"),
                    help="WordPress.org username (plugins author)")
    ap.add_argument("--no-forks", action="store_true", help="hide forked repositories")
    ap.add_argument("--exclude", default=os.environ.get("EXCLUDE_REPOS", ""),
                    help="comma-separated repository names to hide")
    ap.add_argument("--badge", default="100 Days Badge 2026",
                    help="static line kept at the end of the LeetCode block ('' to drop)")
    args = ap.parse_args()

    with open(args.readme, encoding="utf-8") as f:
        text = original = f.read()

    attempted = ok = 0

    if args.github_user:
        attempted += 1
        try:
            repos = fetch_repos(args.github_user, os.environ.get("GITHUB_TOKEN"))
            exclude = {n.strip().lower() for n in args.exclude.split(",") if n.strip()}
            body = build_repos_block(repos, args.github_user, not args.no_forks, exclude)
            text = replace_block(text, "REPOS", body)
            ok += 1
        except Exception as exc:
            print(f"repos block skipped: {exc}", file=sys.stderr)

    if args.wp_user:
        attempted += 1
        try:
            text = replace_block(text, "WPPLUGINS",
                                 build_plugins_block(fetch_plugins(args.wp_user)))
            ok += 1
        except Exception as exc:
            print(f"wordpress plugins block skipped: {exc}", file=sys.stderr)

    if args.leetcode_user:
        attempted += 1
        try:
            text = replace_block(text, "LEETCODE",
                                 build_leetcode_block(args.leetcode_user, args.badge))
            ok += 1
        except Exception as exc:
            print(f"leetcode block skipped: {exc}", file=sys.stderr)

    if not attempted:
        print("Nothing to do: set GITHUB_USER and/or LEETCODE_USERNAME", file=sys.stderr)
        return 2
    if not ok:
        print("All blocks failed, README left unchanged", file=sys.stderr)
        return 1

    if text == original:
        print("README already up to date")
    else:
        with open(args.readme, "w", encoding="utf-8") as f:
            f.write(text)
        print("README updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
