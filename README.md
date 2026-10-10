<table align="center">
  <tr>
    <td valign="top"><img src="assets/terminal-card.svg" alt="ASCII portrait of Haitham Mohamed" width="430"/></td>
    <td valign="top"><img src="assets/info-card.svg" alt="neofetch-style info card: Applied AI Engineer / Architect, Dubai" width="470"/></td>
  </tr>
</table>

<p align="center">
  <img src="assets/contributions.svg" alt="GitHub contribution calendar" width="850"/>
</p>

<div align="center">

<h3>Applied AI Engineer / Architect</h3>
<p><i>Generative AI · RAG · Agent Orchestration · LLM Evaluation — production systems for government, healthcare and social media in the UAE.</i></p>

<p>
  <a href="https://haitham72.github.io"><img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=githubpages&logoColor=white" alt="Portfolio"/></a>
  <a href="mailto:ihisam@outlook.com"><img src="https://img.shields.io/badge/Email-0078D4?style=for-the-badge&logo=microsoftoutlook&logoColor=white" alt="Email"/></a>
  <a href="https://www.linkedin.com/in/haitham72/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="https://neohealth-gpzo.onrender.com"><img src="https://img.shields.io/badge/ReguLense_Live-46E3B7?style=for-the-badge&logo=render&logoColor=black" alt="ReguLense live demo"/></a>
</p>

<img src="https://komarev.com/ghpvc/?username=haitham72&color=39d353&style=flat-square&label=profile+views" alt="Profile views"/>

</div>

<br/>

<h2 align="center">About Me</h2>

<table width="100%">
<tr>
<td width="48%" valign="top">

### Who am I?

- **Customer-facing AI engineer and architect** — 15+ years translating complex stakeholder needs into production systems.
- **Architected and shipped a production Arabic RAG platform** for a Dubai government office: hybrid search, multi-agent orchestration, versioned prompts, regression-gated evaluation.
- **External AI consultant** — took ReguLense from a scoped use case to a live production system for a healthcare advisory firm.
- **Arabic NLP depth** — tashkeel handling, morphological normalization, dialect detection (MSA, Gulf, Nabati, Egyptian), polysemy resolution.
- **Studying** — DBA in AI (Walsh College) and the UT Austin Post Graduate Program in AI & ML. MCA, Amity University.

> *Discovery → architecture → demo → handover. I build the system, then make sure the people who own it can run it.*

</td>
<td width="52%" align="center" valign="middle">

<img src="assets/rag-pipeline.svg" alt="Animated diagram: query → hybrid retrieval → RRF fusion → rerank → validator gate → cited answer" width="100%"/>

</td>
</tr>
</table>

<h2 align="center">Tech Stack</h2>

<table width="100%">
  <tr>
    <td width="50%" valign="top">
      <h3>Languages & Backend</h3>
      <img src="https://skillicons.dev/icons?i=python,fastapi,ts,react,git" alt="Python, FastAPI, TypeScript, React, Git"/>
      <br/><br/>
      <h3>Data & Vectors</h3>
      <img src="https://skillicons.dev/icons?i=postgres,supabase,redis" alt="PostgreSQL, Supabase, Redis"/>
      <br/><sub>pgvector · hybrid search · full-text search · embeddings</sub>
      <br/><br/>
      <h3>Cloud & Delivery</h3>
      <img src="https://skillicons.dev/icons?i=docker,aws,vercel" alt="Docker, AWS, Vercel"/>
    </td>
    <td width="50%" valign="top">
      <h3>LLMs & Agents</h3>
      <p>
        <img src="https://img.shields.io/badge/Claude_API-D97757?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude API"/>
        <img src="https://img.shields.io/badge/OpenAI_API-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI API"/>
        <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" alt="LangGraph"/>
        <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain"/>
        <img src="https://img.shields.io/badge/MCP-000000?style=for-the-badge&logo=modelcontextprotocol&logoColor=white" alt="Model Context Protocol"/>
        <img src="https://img.shields.io/badge/n8n-EA4B71?style=for-the-badge&logo=n8n&logoColor=white" alt="n8n"/>
      </p>
      <sub>Agentic workflows · tool calling · task decomposition · validator gates · human-in-the-loop</sub>
      <h3>Retrieval & Evaluation</h3>
      <p>RAG · Reciprocal Rank Fusion · multi-stage reranking · chunking strategies · Docling · precise citations · LLM evaluation harnesses · regression testing · LangSmith tracing</p>
      <h3>Arabic NLP</h3>
      <p>Morphological normalization · tashkeel handling · dialect detection · code-switching detection · polysemy resolution · text classification</p>
    </td>
  </tr>
</table>

<h2 align="center">Featured Projects</h2>

<table width="100%">
  <tr>
    <td width="50%" valign="top">
      <h3>Hamdan</h3>
      <p>Production Arabic RAG &amp; agentic system for a Dubai government office.</p>
      <p><code>Python</code> <code>LangGraph</code> <code>FastAPI</code> <code>pgvector</code> <code>n8n</code> <code>LangSmith</code> <code>AWS</code></p>
      <ul>
        <li>4-signal hybrid retrieval (semantic + lexical + entity + emotion), RRF, multi-stage reranking</li>
        <li>Research agents, editor agents and a validator gate with cross-category regression testing</li>
        <li>Self-healing prompts: versioned, auto-evaluated, regression-gated</li>
        <li>150+ query evaluation harness with Arabic polysemy test suites</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://neohealth-gpzo.onrender.com">ReguLense</a> · <a href="https://github.com/haitham72/NeoHealth">code</a></h3>
      <p>Version- and jurisdiction-aware RAG for UAE health regulation. Live.</p>
      <p><code>Python</code> <code>FastAPI</code> <code>pgvector</code> <code>OpenAI</code> <code>React</code> <code>Docling</code> <code>Docker</code></p>
      <ul>
        <li>pgvector + PostgreSQL full-text fused via RRF; abstains below a calibrated confidence floor</li>
        <li>Tracks in-force vs. superseded versions; DHA / DoH / MOHAP filter</li>
        <li>PDF citation highlighting from per-element bounding boxes stored at ingest</li>
        <li>Automatic failover to a backup LLM provider, per-client rate capping</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>Mirsal Builder</h3>
      <p>Local, private AI Telegram sticker-generation platform.</p>
      <p><code>Python</code> <code>FastAPI</code> <code>LangGraph</code> <code>pgvector</code> <code>Redis</code> <code>React</code></p>
      <ul>
        <li>LangGraph chat over Studio functions with human approval gates G1–G5</li>
        <li>Ticket-first paid provider calls so a crash never double-charges</li>
        <li>44 deterministic checks across 9 stages, Telegram pack delivery</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h3>Faz3</h3>
      <p>Arabic comment classification for large-scale social media moderation.</p>
      <p><code>Python</code> <code>Supabase</code> <code>Arabic NLP</code></p>
      <ul>
        <li>Dialect-aware classification (MSA, Gulf, Egyptian) with code-switching detection</li>
        <li>Confidence scoring and a human-in-the-loop moderator queue</li>
        <li>941 comments in 32.6 s; human escalation cut from 41% to 10.5%</li>
      </ul>
    </td>
  </tr>
</table>

<h2 align="center">Engineering Experience</h2>

<table width="100%">
  <tr>
    <td width="33%" valign="top">
      <h3>Retrieval</h3>
      <ul>
        <li>Hybrid &amp; semantic search</li>
        <li>Reciprocal Rank Fusion</li>
        <li>Multi-stage reranking</li>
        <li>Structure-aware chunking</li>
        <li>Confidence abstention</li>
        <li>Precise citations</li>
      </ul>
    </td>
    <td width="33%" valign="top">
      <h3>Agents &amp; Evaluation</h3>
      <ul>
        <li>Multi-agent orchestration</li>
        <li>Validator gates</li>
        <li>Self-healing prompts</li>
        <li>Regression-gated releases</li>
        <li>Error taxonomies</li>
        <li>Observability &amp; tracing</li>
      </ul>
    </td>
    <td width="34%" valign="top">
      <h3>Delivery</h3>
      <ul>
        <li>Technical discovery</li>
        <li>Solution architecture</li>
        <li>Stakeholder demos</li>
        <li>Documentation &amp; handover</li>
        <li>LLM provider failover</li>
        <li>Containerized deployments</li>
      </ul>
    </td>
  </tr>
</table>

<h2 align="center">GitHub Activity</h2>

<div align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=haitham72&theme=github_dark" alt="Repos per language"/>
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=haitham72&theme=github_dark" alt="Most commit language"/>
  <br/>
  <img src="https://streak-stats.demolab.com/?user=haitham72&theme=github-dark-blue&hide_border=true&background=0D1117" alt="GitHub streak" width="97%"/>
  <br/>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/haitham72/haitham72/output/snake-dark.svg"/>
    <img src="https://raw.githubusercontent.com/haitham72/haitham72/output/snake.svg" alt="Contribution snake" width="97%"/>
  </picture>
</div>

<br/>

<div align="center">
  <b>Open to Senior / Mid AI Engineer roles — UAE & GCC, remote EU/US.</b>
  <br/><sub>Arabic (native) · English (professional)</sub>
</div>
