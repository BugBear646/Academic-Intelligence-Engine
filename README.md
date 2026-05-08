# 🎓 Academic Intelligence Engine

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4.1-green?style=flat-square&logo=openai)
![Playwright](https://img.shields.io/badge/Playwright-WebCrawler-purple?style=flat-square)
![SQLite](https://img.shields.io/badge/SQLite-Database-orange?style=flat-square&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-red?style=flat-square)

> AI-powered academic faculty crawler for discovering professors, extracting research intelligence, parsing CVs, identifying outreach-ready contacts, and generating ranked university datasets.

</div>

---

## 🌍 Overview

Academic Intelligence Engine is a deep academic crawler built for:
- research internship discovery,
- academic networking,
- faculty outreach,
- professor intelligence gathering,
- research collaboration discovery.

The engine recursively crawls:
- faculty directories,
- professor profiles,
- personal websites,
- CV PDFs,
- academic bios,

and enriches the extracted information using OpenAI models.

---

## ✨ Features

- 🔍 Dynamic faculty discovery
- 🌐 Infinite scrolling support
- 🧠 AI metadata enrichment
- 📄 CV & resume parsing
- 📧 Advanced email extraction
- 🏆 Faculty scoring engine
- 🗂️ University-specific databases
- 🚫 Duplicate prevention
- 📊 CSV exports
- ⚡ Lazy-loading stabilization detection

---

## 🏗️ Project Architecture

```text
academic-intelligence-engine/
│
├── app/
│   │
│   ├── crawler/
│   │   ├── faculty_crawler.py
│   │   ├── profile_parser.py
│   │   ├── pdf_extractor.py
│   │   └── university_sources.py
│   │
│   ├── enrichment/
│   │   ├── llm_extractor.py
│   │   ├── scorer.py
│   │   └── exporter.py
│   │
│   ├── database/
│   │   ├── db.py
│   │   ├── models.py
│   │   ├── clear_db.py
│   │   └── remove_duplicates.py
│   │
│   └── main.py
│
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation Guide

**1️⃣ Clone Repository**

```bash
git clone <your-repository-url>
```

Move into project:

```bash
cd academic-intelligence-engine
```

---

**2️⃣ Create Virtual Environment**

**🍎 macOS / Linux**

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

**🪟 Windows**

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

**3️⃣ Upgrade pip**

```bash
pip install --upgrade pip
```

---

**4️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

---

**5️⃣ Install Playwright Browsers**

```bash
playwright install
```

---

## 🔑 OpenAI API Setup

This project uses OpenAI APIs for:
- metadata extraction,
- expertise classification,
- research summarization,
- structured JSON generation.

---

**6️⃣ Create `.env` File**

Create:

```text
.env
```

inside project root.

Add:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

**7️⃣ Generate OpenAI API Key**

Get API key from:

https://platform.openai.com/api-keys

---

## ⚠️ Important API Notes

API usage depends on:
- your OpenAI billing plan,
- quota,
- rate limits,
- model availability.

This repository does NOT provide:
- bundled credits,
- proxy APIs,
- shared API access.

You are responsible for:
- your API billing,
- quota management,
- OpenAI policy compliance.

---

## ▶️ Running The Crawler

Start crawler:

```bash
python -m app.main
```

---

## 🏛️ University Selection

You will see:

```text
AVAILABLE UNIVERSITIES

1. Stanford Graduate School of Business
2. MIT Sloan
3. Harvard Business School
...more
```

Select university:

```text
Enter university number:
```

Then confirm:

```text
Proceed with crawling? (yes/no):
```

---

## 🔄 Crawl Execution Flow

```text
Faculty Directory
↓
Infinite Scroll
↓
Faculty Profile Extraction
↓
Personal Website Crawl
↓
CV Discovery
↓
PDF Parsing
↓
Email Extraction
↓
AI Metadata Enrichment
↓
Faculty Scoring
↓
CSV Export
↓
SQLite Database Save
```

---

## 📬 Validation Rules

A professor record is valid only if:

✅ Valid professor name  
✅ Valid email  

Plus at least ONE of:
- department
- expertise
- research_interests

---

## 📧 Email Validation

The crawler automatically rejects:
- malformed emails,
- fake placeholder emails,
- duplicate emails,
- invalid syntax.

Examples rejected:

```text
abc
test@
example@email.com
noreply@stanford.edu
```

---

## 📊 Output Files

**🗄️ SQLite Database**

```text
stanford_graduate_school_of_business_professors.db
```

**📄 CSV Export**

Generated inside:

```text
data/exports/
```

Example:

```text
stanford_graduate_school_of_business_professors.csv
```

---

## 🧹 Database Utilities

**Remove Duplicate Records**

```bash
python -m app.database.remove_duplicates
```

---

**Clear Database**

```bash
python -m app.database.clear_db
```

This:
- deletes all records,
- preserves schema,
- asks for confirmation.

---

## 🛠️ Common Installation Issues

**❌ Playwright Not Installed**

```text
playwright: command not found
```

Fix:

```bash
pip install playwright
```

Then:

```bash
playwright install
```

---

**❌ lxml Build Errors (macOS)**

Fix:

```bash
pip install wheel
```

Then retry:

```bash
pip install -r requirements.txt
```

---

**❌ Missing OpenAI API Key**

```text
OPENAI_API_KEY not found
```

Fix:
- create `.env`,
- add valid API key.

---

## 💻 Recommended Environment

Recommended:
- Python 3.10+
- macOS / Linux
- VSCode
- SQLite Browser

---

## 🧰 Technologies Used

- Python
- Playwright
- BeautifulSoup
- Requests
- SQLAlchemy
- SQLite
- OpenAI API
- Pandas

---

## 🚀 Future Improvements

Potential upgrades:
- async crawling,
- Redis queues,
- semantic vector search,
- research-paper extraction,
- publication scoring,
- embeddings-based ranking,
- outreach automation,
- multi-university orchestration.

---

## 🤝 Open For Contributions

Contributions are welcome.

Areas where contributions would help:
- support for more universities,
- async crawling,
- publication extraction,
- semantic search,
- retry pipelines,
- faculty recommendation systems,
- outreach automation,
- dashboard UI,
- proxy support,
- ranking improvements.

---

## ⚖️ Ethical Usage

### ❌ Do NOT:
- spam professors,
- misuse extracted emails,
- violate university policies,
- aggressively scrape protected systems.

### ✅ Recommended use:
- academic networking,
- research collaboration,
- internship discovery,
- educational outreach.
