# Hi, I'm Pavel Silinskii 👋

**Full-Stack PHP Developer (Laravel, WordPress) · expanding into AI-powered applications**

Based in Needham, MA US. 15+ years building web applications, e-commerce platforms, and API integrations.
Now building production-minded Python LLM applications: RAG, structured extraction with human review, agents with a deterministic policy layer, an MCP server, Redis caching and rate limits, chat history on MongoDB and DynamoDB, OpenTelemetry, Prometheus and Grafana monitoring, Kubernetes manifests, and CI/CD that proves what is deployed. Each project ships with tests, Docker, CI and evidence from real runs.

## 🛠️ Tech Stack

**Backend**

![PHP](https://img.shields.io/badge/PHP-777BB4?style=flat&logo=php&logoColor=white)
![Laravel](https://img.shields.io/badge/Laravel-FF2D20?style=flat&logo=laravel&logoColor=white)
![WordPress](https://img.shields.io/badge/WordPress-21759B?style=flat&logo=wordpress&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white)
![DynamoDB](https://img.shields.io/badge/DynamoDB-4053D6?style=flat&logo=amazondynamodb&logoColor=white)
![REST API](https://img.shields.io/badge/REST_API-02569B?style=flat)
![Stripe](https://img.shields.io/badge/Stripe-635BFF?style=flat&logo=stripe&logoColor=white)

**Frontend**

![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![React](https://img.shields.io/badge/React-learning-61DAFB?style=flat&logo=react&logoColor=black)
![Vue.js](https://img.shields.io/badge/Vue.js-learning-4FC08D?style=flat&logo=vuedotjs&logoColor=white)

**Tools & DevOps**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=flat&logo=swagger&logoColor=black)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat&logo=grafana&logoColor=white)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-425CC7?style=flat&logo=opentelemetry&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-learning-232F3E?style=flat&logo=amazonwebservices&logoColor=white)

**AI / Python**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Anthropic](https://img.shields.io/badge/Anthropic_API-412991?style=flat)
![Groq](https://img.shields.io/badge/Groq_API-F55036?style=flat)
![AWS Bedrock](https://img.shields.io/badge/AWS_Bedrock-232F3E?style=flat&logo=amazonwebservices&logoColor=white)
![RAG](https://img.shields.io/badge/RAG-0A7B83?style=flat)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat)
![MCP](https://img.shields.io/badge/MCP-000000?style=flat)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6446?style=flat)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white)

## 🚀 Featured Projects

### [RAG Assistant](https://github.com/pavelsilinskiiwork/rag-assistant) · [🔗 Live demo](https://pavelsilinskiiwork.github.io/rag-assistant/)
Question answering over your own documents: semantic search, source and page citations, web chat, REST API and a tool-calling agent. Runs on Claude, Groq or AWS Bedrock models behind one provider interface

[![tests](https://github.com/pavelsilinskiiwork/rag-assistant/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/pavelsilinskiiwork/rag-assistant/actions/workflows/tests.yml)

- Public demo: GitHub Pages UI + FastAPI on Render, with per-IP and daily rate limits, uploads disabled, provider fallback and spending caps
- FastAPI service with Swagger · PDF upload with page-level citations `[file.pdf, p. 3]`
- Three-layer hallucination guard: distance threshold, relative margin around the best chunk, "answer only from context" prompt
- Retrieval evaluation (8 cases); smaller chunks improved the distance on a key query from 0.81 to 0.57
- Agent with tool calling and prompt-injection defenses; live eval of 5 attacks per model: 5/5 resisted on Claude Haiku and gpt-oss-120b, 0-2/5 on Amazon Nova Lite (no attack succeeded, but its platform filter blocked answers)
- Three providers behind one interface: Anthropic, Groq and AWS Bedrock (Converse API with tool use)
- Structured logs with latency, tokens and cost per request
- pytest · GitHub Actions CI · Docker Compose
- Python · FastAPI · ChromaDB · Anthropic API · Groq API · AWS Bedrock

### [Document Extraction](https://github.com/pavelsilinskiiwork/doc-extraction)
Invoices (PDF or text) to validated, structured JSON with an LLM. The model proposes values, Pydantic enforces the business rules, and a failed check goes back to the model as a precise error for a corrected retry. Every run is stored and risky ones go to a human review queue

[![tests](https://github.com/pavelsilinskiiwork/doc-extraction/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/pavelsilinskiiwork/doc-extraction/actions/workflows/tests.yml)

- FastAPI `POST /extract` · schema with arithmetic checks (line amounts, subtotal, discount, tax, total) · money as `Decimal`
- Retry with validation feedback · document text treated as untrusted input (a sample invoice carries an injected instruction)
- PostgreSQL + Docker Compose: every run stored with the original text, model output and cost; the model's answer is never overwritten, reviewer fixes are kept separately
- Review queue: retries, large totals, injection-like text and possible duplicates are flagged with reasons · approve / correct / reject API · API-key protection
- Accuracy two ways: labelled synthetic invoices (100% on gpt-oss-120b, 98.8% on Amazon Nova Lite, 14 documents, small and easy set) and live review decisions per provider
- Same provider layer as RAG Assistant: Anthropic, Groq and AWS Bedrock
- Python · FastAPI · Pydantic · PostgreSQL · SQLAlchemy · Docker Compose · pytest (63 tests) · GitHub Actions CI

### [LLM Cache, Rate Limit and Budget](https://github.com/pavelsilinskiiwork/llm-cache-ratelimit)
Redis-backed controls in front of an LLM call: a response cache, a per-client rate limit and a daily spending cap

[![tests](https://github.com/pavelsilinskiiwork/llm-cache-ratelimit/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/pavelsilinskiiwork/llm-cache-ratelimit/actions/workflows/tests.yml)

- Single-flight cache: 20 identical concurrent requests make one model call
- Sliding-window rate limit in one Redis transaction, correct across several API processes · 429 with `Retry-After`
- Daily budget with reserve-then-settle in integer micro-dollars: concurrent requests cannot overshoot the cap; cached answers keep working after it is spent
- Explicit failure policy: cache fails open, limits and budget fail closed (503) unless `FAIL_OPEN=true`
- Benchmark against a simulated 300 ms model: 300 requests needed 37 model calls instead of 300 (87.7% hit rate)
- Python · FastAPI · Redis · Docker Compose · pytest (79 tests, fakeredis and real Redis) · GitHub Actions CI

### [FastAPI to Render CI/CD](https://github.com/pavelsilinskiiwork/fastapi-render-cicd)
A GitHub Actions pipeline that deploys only after every check passes, then proves the new commit is the one running in production

[![pipeline](https://github.com/pavelsilinskiiwork/fastapi-render-cicd/actions/workflows/pipeline.yml/badge.svg?branch=main)](https://github.com/pavelsilinskiiwork/fastapi-render-cicd/actions/workflows/pipeline.yml)

- Jobs: lint, tests on Python 3.11-3.13 with a coverage gate, Docker build and smoke test, a Kubernetes rollout check, then deploy
- Kubernetes manifests (Deployment, Service, HPA, PodDisruptionBudget): CI validates them, rolls them out to a throw-away kind cluster and runs the same smoke test through the Service (a local cluster, not a managed one)
- Deploy hook for the exact commit, then a smoke test polls `/version` until production reports that commit and `/health` is ok
- Verified with real runs: a broken test and a broken Dockerfile each stopped the pipeline before deploy
- Least-privilege token, protected `production` environment, Dependabot, one deploy at a time
- Python · FastAPI · GitHub Actions · Docker · Render

### [Support Triage Agent](https://github.com/pavelsilinskiiwork/support-triage-agent)
A LangGraph agent that triages support tickets, with a deterministic policy between the model and the tools, evaluated against simpler designs on tickets that include prompt-injection attempts

[![CI](https://github.com/pavelsilinskiiwork/support-triage-agent/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/pavelsilinskiiwork/support-triage-agent/actions/workflows/ci.yml)

- Graph: guard, classify, BM25 runbook retrieval, plan, verify, execute or escalate; only classify and plan call a model
- Policy in plain code: refunds allowed only from trusted helpdesk metadata (charge age and amount), 2FA and email changes never automatic, replies must cite runbooks and may only contain links found in them, fail closed on any model error
- Three variants compared on 46 labelled tickets (16 attacks): one naive call, one call plus the same policy, and the graph
- Offline run with a stand-in model that obeys every injection: 17 of 24 risky tickets end unsafely with the naive agent, 1 of 24 with the policy
- Live run on Claude Haiku (3 repeats): no unsafe outcome in any variant, so the attacks did not move this model; the graph was slightly more accurate but the gap rests on 2 or 3 tickets. Stated that way in the README, with its limits
- Python · LangGraph · Pydantic · Anthropic, Bedrock and Groq adapters · pytest (102 tests) · GitHub Actions CI

### [MCP Invoice Server](https://github.com/pavelsilinskiiwork/mcp-invoice-server)
A Model Context Protocol server that lets an AI client review invoices from the doc-extraction API, built so that invoice text cannot talk the client into approving anything

[![CI](https://github.com/pavelsilinskiiwork/mcp-invoice-server/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/pavelsilinskiiwork/mcp-invoice-server/actions/workflows/ci.yml)

- Read tools by default; write tools (approve, correct, reject) are opt-in, show a preview first and need an explicit confirm, with a per-session write cap
- Fail-closed audit log: if the audit record cannot be written, the write does not happen
- Document text is labelled as untrusted and scanned for injection-like phrases; the API stays the authority, the server holds no business rules
- Contract tests run against the real doc-extraction API in CI · stdio and streamable HTTP transports · demo client script
- Python · MCP SDK · httpx · Pydantic · pytest with a coverage gate · GitHub Actions CI

### [LLM Observability Stack](https://github.com/pavelsilinskiiwork/llm-observability-stack)
Prometheus metrics, OpenTelemetry traces, a Grafana dashboard defined as code and tested alert rules for an LLM service, with a load script that breaks it on purpose

[![CI](https://github.com/pavelsilinskiiwork/llm-observability-stack/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/pavelsilinskiiwork/llm-observability-stack/actions/workflows/ci.yml)

- Metrics: requests, latency histogram, tokens, cost, in-flight requests and daily spend against a budget, with low-cardinality labels
- Five alert rules with promtool unit tests; the dashboard is generated by a script and CI fails if the committed JSON drifts
- Load script with failing and slow phases: in a real run the error-rate alert fired about a minute after failures began and the latency alert about 65 seconds after the slow phase started (screenshots in the README)
- OpenTelemetry: one trace per request with a child span around the model call (GenAI attribute names, the prompt is never recorded), exported to Grafana Tempo; CI sends a request and checks that its trace is stored
- Docker Compose brings up the app, Prometheus, Tempo and Grafana; CI starts them and checks that every dashboard query returns data
- No Alertmanager yet, so alerts are visible but do not notify anyone; traces are not sampled (stated in the README)
- Python · FastAPI · OpenTelemetry · Tempo · Prometheus · Grafana · Docker Compose · pytest (43 tests) · GitHub Actions CI

### [LLM Conversation Store](https://github.com/pavelsilinskiiwork/llm-conversation-store)
Chat history for LLM applications on MongoDB or DynamoDB behind one interface, with a retention period on every message

[![CI](https://github.com/pavelsilinskiiwork/llm-conversation-store/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/pavelsilinskiiwork/llm-conversation-store/actions/workflows/ci.yml)

- Layouts chosen for the access pattern: "last N messages" is one indexed query in MongoDB and one `Query` with `Limit` in DynamoDB, no scans
- Expiry is also enforced on read, because MongoDB's TTL monitor and DynamoDB's TTL deletion are lazy; tested with a fake clock in every backend
- One contract test suite for memory, mongomock, moto and, in CI, a real MongoDB and DynamoDB Local
- Not tried on AWS itself or MongoDB Atlas (stated in the README)
- Python · pymongo · boto3 · pytest (56 tests) · GitHub Actions CI

### [Job Application Tracker API](https://github.com/pavelsilinskiiwork/job-tracker-api)
REST API for tracking job applications with status management and statistics

- JWT authentication · CRUD for job listings · Status flow tracking
- Application statistics and funnel analytics
- Swagger UI documentation · 19 automated tests · Docker Compose

### [E-Commerce API](https://github.com/pavelsilinskiiwork/ecommerce-api)
Full-featured e-commerce backend with Stripe payment integration

- Product catalog with filtering · Shopping cart · Order management
- Stripe Payment Intent + webhook handling · Stock management
- Swagger UI documentation · 24 automated tests · Docker Compose

### [Advanced Contact Forms](https://github.com/pavelsilinskiiwork/advanced-contact-forms)
WordPress plugin with drag-and-drop form builder and REST API

- Drag-and-drop form builder · 7 field types · Database storage
- Email notifications · REST API · CSV export · Honeypot spam protection
- Shortcode `[contact_form id="1"]` · Clean admin panel

<!-- Add Laravel projects here, same format as above -->

## 📚 All Repositories

<!--REPOS:START-->
- [**llm-conversation-store**](https://github.com/pavelsilinskiiwork/llm-conversation-store) — Chat history for LLM apps on MongoDB and DynamoDB with TTL. One contract test suite, run against real databases in CI. · `Python`
- [**wp-maintenance-mode**](https://github.com/pavelsilinskiiwork/wp-maintenance-mode) — Lightweight WordPress maintenance mode plugin: SEO-safe 503 + Retry-After, countdown with auto-disable, custom page, and access by role, IP whitelist or secret bypass link. No external scripts, no tracking. · `PHP`
- [**doc-extraction**](https://github.com/pavelsilinskiiwork/doc-extraction) — LLM invoice extraction with schema validation, arithmetic checks, retry, PostgreSQL storage and a human review queue. Claude, Groq and AWS Bedrock providers. · `Python`
- [**rag-assistant**](https://github.com/pavelsilinskiiwork/rag-assistant) — RAG question answering over documents: FastAPI, ChromaDB, PDF page citations, tool-calling agent with prompt-injection defenses, Claude, Groq and AWS Bedrock providers, live demo · `Python`
- [**wp-social-share**](https://github.com/pavelsilinskiiwork/wp-social-share) — Lightweight social share buttons for WordPress: Facebook, Twitter/X, LinkedIn, Pinterest, WhatsApp, plus a Copy Link button. No external scripts, no jQuery, no tracking, no cookies — inline SVG icons and vanilla JavaScript. · `PHP`
- [**wp-popup-builder**](https://github.com/pavelsilinskiiwork/wp-popup-builder) — Lightweight popup builder for WordPress. Create popups for promotions, newsletter signups, and announcements with flexible trigger and display rules. · `PHP`
- [**pavel-silinskii-cookie-consent**](https://github.com/pavelsilinskiiwork/pavel-silinskii-cookie-consent) — Lightweight GDPR/CCPA cookie consent banner for WordPress with bar and popup layouts, light/dark themes, and one-click accept/decline. No external requests, no tracking, vanilla JavaScript on the frontend. · `PHP`
- [**wp-age-verification**](https://github.com/pavelsilinskiiwork/wp-age-verification) — Age verification popup for WordPress. Shows a verification gate when a visitor enters the site (or selected pages/categories). · `PHP`
- [**advanced-contact-forms**](https://github.com/pavelsilinskiiwork/advanced-contact-forms) — WordPress plugin for creating contact forms with drag-and-drop builder, database storage, REST API and CSV export · `PHP`
- [**python-basics**](https://github.com/pavelsilinskiiwork/python-basics) — Python fundamentals: console expense tracker with CSV persistence · `Python`
- [**ecommerce-api**](https://github.com/pavelsilinskiiwork/ecommerce-api) — Laravel.E-commerce REST API with Stripe payment integration, shopping cart, order management and 24 automated tests · `PHP`
- [**boilerplate-npm**](https://github.com/pavelsilinskiiwork/boilerplate-npm) — A boilerplate for the freeCodeCamp curriculum. · `JavaScript` · fork
- [**job-tracker-api**](https://github.com/pavelsilinskiiwork/job-tracker-api) — REST API for tracking job applications — built with Laravel 13, JWT authentication, and Docker support. · `PHP`
<!--REPOS:END-->

## 🧩 WordPress Plugins

   <!--WPPLUGINS:START-->
- [**Pavel Silinskii Age Verification**](https://wordpress.org/plugins/pavel-silinskii-age-verification/) — Age verification popup for WordPress. Supports Yes/No and date of birth verification modes, with block or redirect on decline.
- [**Pavel Silinskii Contact Forms**](https://wordpress.org/plugins/pavel-silinskii-contact-forms/) — A powerful contact form plugin with a drag-and-drop builder, database storage, email notifications, REST API, and CSV export of submissions.
- [**Pavel Silinskii Cookie Consent**](https://wordpress.org/plugins/pavel-silinskii-cookie-consent/) — Lightweight GDPR/CCPA cookie consent banner with bar and popup layouts, light/dark themes, and one-click accept/decline.
- [**Pavel Silinskii Popup Builder**](https://wordpress.org/plugins/pavel-silinskii-popup-builder/) — Lightweight popup builder for WordPress. Create popups for promotions, newsletter signups, and announcements.
- [**Pavel Silinskii Social Share**](https://wordpress.org/plugins/pavel-silinskii-social-share/) — Lightweight social share buttons for WordPress. No external scripts, no tracking, GDPR-friendly.
<!--WPPLUGINS:END-->

## 📜 Certifications

- 🏆 freeCodeCamp — JavaScript Algorithms and Data Structures
- 🏆 freeCodeCamp — Responsive Web Design
- 🏆 [Kaggle — Python](https://www.kaggle.com/learn/certification/pavelsilinskii26/python)
- 🏆 [Google Cloud — Introduction to Generative AI](https://partner.skills.google/public_profiles/de745e7c-ad5e-4b78-9747-ea58cfefe067/badges/26811194)
- 📚 AWS Cloud Practitioner Essentials — in progress

## 💻 LeetCode

<!--LEETCODE:START-->
- ✅ 55 Easy · 129 Medium · 39 Hard
- 🔥 Current streak: 57 days · 195 active days
- 🏅 100 Days Badge 2026
<!--LEETCODE:END-->

## 📊 GitHub Stats

![Top languages](https://github-readme-stats.vercel.app/api/top-langs/?username=pavelsilinskiiwork&layout=compact)

## 🗺️ What's Next

- 📄 Document extraction: harder documents (scans, multi-page) and a simple review UI
- 🔎 RAG Assistant: reranking and answer-level evaluation with Ragas
- ☁️ AWS: Cloud Practitioner, then Bedrock-based deployments
- 🅻 Laravel projects (APIs and full-stack apps)
- 🧩 More open-source WordPress plugins

## 📫 Let's Connect

Open to remote PHP/Full-Stack Developer positions, Applied AI / LLM-integration backend roles, and freelance projects.
