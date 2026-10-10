<div align="center">

  <!-- ASCII Art Portrait -->
  <pre>
  _    _                 _
  | |  | |               | |
  | |__| | ___  _ __   __| | __ _ _   _
  |  __  |/ _ \| '_ \ / _` |/ _` | | | |
  | |  | | (_) | | | | (_| | (_| | |_| |
  |_|  |_|\___/|_| |_|\__,_|\__,_|\__, |
                                      __/ |
                                     |___/
  </pre>

  <!-- Info Card -->
  <img src="https://raw.githubusercontent.com/salesforce/boxericons/main/svg/filled/Coding.svg" width="150" alt="Coding" />

### **Applied AI Engineer & Architect**

Building production-grade Generative AI, RAG systems, and agentic workflows at scale.

[![Email](https://img.shields.io/badge/Email-ihisam@outlook.com-blue?style=for-the-badge&logo=microsoft-outlook)](mailto:ihisam@outlook.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-haitham72-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/haitham72)
[![GitHub](https://img.shields.io/badge/GitHub-haitham72-white?style=for-the-badge&logo=github)](https://github.com/haitham72)

![Visitor Count](https://profile-counter.glitch.me/haitham72/count.svg)

</div>

---

## 🚀 About Me

<div align="center">

### 👨‍💻 Who am I?

- 🎯 **Applied AI Engineer & Architect** with 15+ years of professional experience translating complex stakeholder needs into production systems
- 💻 **Hands-on builder** of Generative AI, RAG, agent orchestration, and LLM evaluation frameworks
- 🌍 **Based in Dubai, UAE** — Native Arabic, Professional English
- 🎓 **DBA in AI (In Progress)** — Walsh College | Post Graduate Program in AI/ML — UT Austin
- 🚀 Currently building production-ready AI systems with hybrid search, multi-agent orchestration, and regression-gated evaluation
- 🇦🇪 **Unfair Advantage:** Deep Arabic NLP expertise (tashkeel handling, dialect detection, polysemy resolution)

> "I don't just write code. I build scalable AI solutions that solve real-world problems, with precise citations and production resilience."

</div>

---

## 🏅 Key Achievements

- 🏆 **Architected & Shipped** a production Arabic RAG platform for Dubai government office (Nadi) — hybrid search, multi-agent orchestration, self-healing prompts
- 🎯 **150+ Query LLM Evaluation Harness** with regression gating and Arabic-specific polysemy test suites
- 📊 **Real-Data Throughput:** 941 comments processed in 32.6 seconds at 10.5% human-escalation rate (reduced from 41%)
- 🚀 **Deployed ReguLense** — Version and jurisdiction-aware RAG for UAE health regulation (live on Render)
- 🤖 **Built Mirsal Builder** — AI Telegram sticker generation platform with LangGraph agent orchestration

---

## ⚡ Tech Stack & Engineering Arsenal

<div align="center">

### 🤖 Applied AI & LLM Engineering

Generative AI • Large Language Models (LLMs) • Claude API • OpenAI API • Advanced Prompt Engineering • Evaluation Frameworks • Regression Testing • Self-Healing Prompt Architecture • Deployment at Scale • LangSmith • Observability & Tracing

### 🔍 Retrieval & RAG Systems

Retrieval Augmented Generation (RAG) • Hybrid Search • Semantic Search • Full-Text Search • Embeddings • Vector Databases • PostgreSQL/pgvector • Reciprocal Rank Fusion (RRF) • Multi-Stage Reranking • Chunking Strategies • Precise Citations • Docling

### 🤖 Agent Orchestration

AI Agents • Agentic AI • Multi-Agent Systems • Agentic Workflows • Task Decomposition • Tool Calling • LangChain • LangGraph • Model Context Protocol (MCP) • Validator Gates • Human-in-the-Loop Design

### 🗄️ Engineering & Cloud

Python • FastAPI • API Development • REST APIs • Docker • AWS • Git • PostgreSQL • Supabase • Redis • n8n Workflow Automation • React • TypeScript • Vercel • Render

### 🌍 Arabic NLP

Natural Language Processing (NLP) • Arabic NLP • Morphological Normalization • Tashkeel Handling • Dialect Detection (MSA, Gulf, Nabati, Egyptian) • Polysemy Resolution • Code-Switching Detection • Text Classification

### 🔐 Security & Production Resilience

JWT • Role-Based Access Control (RBAC) • OAuth • Authentication • Authorization • Rate Limiting • Automatic Failover • Per-Client Rate Capping • Production Monitoring

</div>

---

## 📂 Featured Projects

<div align="center">

### 🎭 Hamdan — Production Arabic RAG & Agentic System

- **Hybrid Search:** 4-signal retrieval (semantic + lexical + entity + emotion) with reciprocal rank fusion and multi-stage reranking
- **Multi-Agent Architecture:** Research agents (read-only), editor agents (single-category ownership), validator gate (cross-category regression testing)
- **Self-Healing Prompts:** Versioned prompt management with automated evaluation, regression gating, and per-category performance tracking
- **Arabic NLP Pipeline:** Tashkeel handling, morphological normalization, dialect detection (MSA / Gulf / Nabati), polysemy resolution

**Tech Stack:** Python, LangGraph, LangChain, FastAPI, PostgreSQL/pgvector, n8n, Docker, AWS, LangSmith

---

### 🏥 ReguLense — Version & Jurisdiction-Aware RAG for UAE Health Regulation

**Live:** [neohealth-gpzo.onrender.com](https://neohealth-gpzo.onrender.com) | **GitHub:** [haitham72/NeoHealth](https://github.com/haitham72/NeoHealth)

- **Hybrid Retrieval with Tiered Confidence:** pgvector cosine similarity + PostgreSQL full-text search fused via RRF; abstains below calibrated confidence floor
- **Version & Jurisdiction Awareness:** Tracks which regulation version is in force vs. superseded; supports DHA / DoH / MOHAP jurisdiction filter
- **Production Resilience:** Automatic failover to backup LLM provider on rate limits/outages, plus per-client rate capping
- **Precise PDF Citation Highlighting:** Structure-aware document chunking (Docling) with exact per-element bounding box provenance

**Tech Stack:** Python, FastAPI, PostgreSQL/pgvector, OpenAI, React, TypeScript, Docling, Docker, AWS

---

### 🎨 Mirsal Builder — AI Telegram Sticker Generation Platform

- **Agent Orchestration:** LangGraph chat over Studio functions, human approval gates G1-G5, vision-model pre-review, ticket-first paid provider calls
- **Retrieval/Vector Infrastructure:** PostgreSQL mirror + pgvector sticker pool, Redis caching, and local embeddings
- **Media Generation:** Integrated via Higgsfield CLI, local multimodal models, and OpenAI fallback
- **Deterministic Verification:** 44 checks across 9 stages, human-in-the-loop "Use it anyway" overrides, and Telegram pack delivery

**Tech Stack:** Python, FastAPI, uvicorn, PostgreSQL/pgvector, Redis, Docker, LangGraph, LangChain, n8n, React, TypeScript, AWS

---

### 💬 Faz3 — Arabic Comment Classification Pipeline

- **Arabic NLP Classification:** Dialect-aware classification (MSA, Gulf, Egyptian) with code-switching detection
- **Human-in-the-Loop:** Confidence scoring and moderator queue for assisted triage
- **Performance:** 941 comments processed in 32.6 seconds at 10.5% human-escalation rate (reduced from 41%)

**Tech Stack:** Python, Supabase, Arabic NLP preprocessing

</div>

---

## 📚 Education

<div align="center">

### 🎓 Doctor of Business Administration (DBA), Artificial Intelligence

**Walsh College, Troy, MI, USA** | In Progress (Dec 2025 - Dec 2027)

### 🎓 Post Graduate Program, Artificial Intelligence & Machine Learning

**UT Austin McCombs School of Business** | In Progress (Started Dec 2025)

### 🎓 Master of Computer Applications (MCA), Computer Software Engineering

**Amity University, Noida, India** | Completed (Jun 2023 - Jun 2025), Grade: Very Good

### 🎓 Bachelor of Fine Arts (Animation)

**Helwan University, Cairo, Egypt** | Completed (2004 - 2009), Grade: Very Good

</div>

---

## 🌐 Let's Connect

<div align="center">

[![Email](https://img.shields.io/badge/📧_Email-ihisam@outlook.com-blue?style=for-the-badge)](mailto:ihisam@outlook.com)
[![LinkedIn](https://img.shields.io/badge/🔗_LinkedIn-haitham72-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/haitham72)
[![GitHub](https://img.shields.io/badge/💻_GitHub-haitham72-white?style=for-the-badge&logo=github)](https://github.com/haitham72)

**Open to:** Senior/Mid AI Engineer roles in UAE/GCC, remote EU/US

</div>

---

<div align="center">

**⭐ Star this repo if you find my work useful!**

![GitHub Stars](https://img.shields.io/github/stars/haitham72/haitham72?style=social)

</div>
