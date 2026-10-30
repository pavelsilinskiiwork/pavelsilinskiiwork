# Hi, I'm Pavel Silinskii 👋

**Full-Stack PHP Developer (Laravel, WordPress) · expanding into AI-powered applications**

Based in Needham, MA US. 15+ years building web applications, e-commerce platforms, and API integrations.
Now building Python LLM applications: RAG, vector search, tool-calling agents, with tests, Docker, CI and a public live demo.

## 🛠️ Tech Stack

**Backend**

![PHP](https://img.shields.io/badge/PHP-777BB4?style=flat&logo=php&logoColor=white)
![Laravel](https://img.shields.io/badge/Laravel-FF2D20?style=flat&logo=laravel&logoColor=white)
![WordPress](https://img.shields.io/badge/WordPress-21759B?style=flat&logo=wordpress&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)
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
![AWS](https://img.shields.io/badge/AWS-learning-232F3E?style=flat&logo=amazonwebservices&logoColor=white)

**AI / Python**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Anthropic](https://img.shields.io/badge/Anthropic_API-412991?style=flat)
![Groq](https://img.shields.io/badge/Groq_API-F55036?style=flat)
![AWS Bedrock](https://img.shields.io/badge/AWS_Bedrock-232F3E?style=flat&logo=amazonwebservices&logoColor=white)
![RAG](https://img.shields.io/badge/RAG-0A7B83?style=flat)
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
Invoices (PDF or text) to validated, structured JSON with an LLM. The model proposes values, Pydantic enforces the business rules, and a failed check goes back to the model as a precise error for a corrected retry

[![tests](https://github.com/pavelsilinskiiwork/doc-extraction/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/pavelsilinskiiwork/doc-extraction/actions/workflows/tests.yml)

- FastAPI `POST /extract` · schema with arithmetic checks (line amounts, subtotal, discount, tax, total) · money as `Decimal`
- Retry with validation feedback · document text treated as untrusted input (a sample invoice carries an injected instruction)
- Labelled synthetic invoices (US/German/UK layouts, PDF and text) and a field-level accuracy eval: 100% on gpt-oss-120b, 98.8% on Amazon Nova Lite (14 documents, small and easy set)
- Same provider layer as RAG Assistant: Anthropic, Groq and AWS Bedrock
- Python · FastAPI · Pydantic · pypdf · pytest · GitHub Actions CI

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
- [**doc-extraction**](https://github.com/pavelsilinskiiwork/doc-extraction) — Invoice extraction from PDF/text into validated JSON: LLM + Pydantic business-rule checks, retry with error feedback, labelled samples and field-level accuracy eval. Claude, Groq and AWS Bedrock providers. · `Python`
- [**wp-maintenance-mode**](https://github.com/pavelsilinskiiwork/wp-maintenance-mode) — Lightweight WordPress maintenance mode plugin: SEO-safe 503 + Retry-After, countdown with auto-disable, custom page, and access by role, IP whitelist or secret bypass link. No external scripts, no tracking. · `PHP`
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
- ✅ 51 Easy · 127 Medium · 39 Hard
- 🔥 Current streak: 57 days · 189 active days
- 🏅 100 Days Badge 2026
<!--LEETCODE:END-->

## 📊 GitHub Stats

![Top languages](https://github-readme-stats.vercel.app/api/top-langs/?username=pavelsilinskiiwork&layout=compact)

## 🗺️ What's Next

- 📄 Document extraction: PostgreSQL storage, review and correction endpoints, harder documents (scans, multi-page)
- 🔎 RAG Assistant: reranking and answer-level evaluation with Ragas
- 🤖 Agent work with LangGraph
- ☁️ AWS: Cloud Practitioner, then Bedrock-based deployments
- 🅻 Laravel projects (APIs and full-stack apps)
- 🧩 More open-source WordPress plugins

## 📫 Let's Connect

Open to remote PHP/Full-Stack Developer positions, Applied AI / LLM-integration backend roles, and freelance projects.
