# 🎓 Academic Intelligence Engine

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4.1-green?style=for-the-badge&logo=openai)
![Playwright](https://img.shields.io/badge/Playwright-Web%20Crawler-purple?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-Database-orange?style=for-the-badge&logo=sqlite)
![MIT License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)

> AI-powered academic faculty crawler for discovering professors, extracting research intelligence, parsing CVs, identifying outreach-ready contacts, and generating ranked university datasets.

</div>

---

## 🌍 Overview

Academic Intelligence Engine is a deep academic crawler designed for:
- research internship discovery,
- academic networking,
- professor outreach,
- faculty intelligence gathering,
- research collaboration discovery.

The engine recursively crawls:
- faculty directories,
- professor profiles,
- personal websites,
- CV PDFs,
- academic bios,

and enriches everything using OpenAI models.

---

## ✨ Core Features

### 🔍 Faculty Discovery
- Dynamic faculty directory crawling
- Infinite scroll support
- Lazy-loaded page handling
- Multi-university architecture

---

### 🧠 AI Metadata Enrichment

Uses OpenAI models to:
- infer expertise,
- summarize research interests,
- structure faculty metadata,
- standardize academic records.

---

### 📄 Recursive CV & Resume Parsing

Crawler flow:

```text
Faculty Profile
↓
Personal Website
↓
Bio / CV Page
↓
Resume PDF
↓
Email Extraction
```

Supports:
- PDF CV extraction,
- personal websites,
- faculty bios,
- external academic pages.

---

### 📧 Advanced Email Discovery

Extracts emails from:
- faculty pages,
- mailto links,
- CV PDFs,
- obfuscated HTML,
- external websites.

---

### 🏆 Faculty Scoring Engine

Ranks professors based on relevance to:
- Product Management
- Platform Strategy
- Innovation
- Organizational Behavior
- Behavioral Economics
- AI Systems
- Consumer Research
- Information Systems

---

### 🗂️ University-Specific Storage

Each university gets:
- dedicated SQLite database,
- dedicated CSV export.

---

## 🏫 Supported Universities

Currently optimized for:

<div align="center">

### Stanford Graduate School of Business

<img src="https://www.gsb.stanford.edu/sites/default/files/styles/1630x_variable/public/resources/photo-campus-overview.jpg.webp?itok=uT4UjZ2n" width="850"/>

---

### MIT Sloan School of Management

<img src="https://mitsloan.mit.edu/sites/default/files/styles/hero_desktop/public/2023-06/hero-campus.jpg.webp" width="850"/>

---

### Harvard Business School

<img src="https://www.hbs.edu/Style%20Library/api/resize.aspx?imgpath=/PublishingImages/campus/aerial-campus.jpg&w=1200" width="850"/>

</div>

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

### 1️⃣ Clone Repository

```bash
git clone <your-repository-url>
```

Move into project:

```bash
cd academic-intelligence-engine
```

---

### 2️⃣ Create Virtual Environment

#### 🍎 macOS / Linux

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

#### 🪟 Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

### 3️⃣ Upgrade pip

```bash
pip install --upgrade pip
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Install Playwright Browsers

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

### 6️⃣ Create `.env` File

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

### 🔐 Generate OpenAI API Key

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

## 🌐 Stanford Lazy Loading Handling

Stanford dynamically loads faculty cards.

The crawler:
- scrolls repeatedly,
- waits 15 seconds after each scroll,
- finalizes only after profile stabilization.

This avoids:
- incomplete extraction,
- partial faculty discovery.

---

## 📬 Validation Rules

A professor record is valid only if:

### ✅ Required
- valid professor name
- valid email

### ➕

At least ONE of:
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

## 🚫 Duplicate Prevention

Duplicates are prevented using:
- faculty URLs,
- professor names,
- professor emails.

---

## 📊 Output Files

### 🗄️ SQLite Database

Example:

```text
stanford_graduate_school_of_business_professors.db
```

---

### 📄 CSV Export

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

### Remove Duplicate Records

```bash
python -m app.database.remove_duplicates
```

---

### Clear Database

```bash
python -m app.database.clear_db
```

This:
- deletes all records,
- preserves schema,
- asks for confirmation.

---

## 🛠️ Common Installation Issues

### ❌ Playwright Not Installed

Error:

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

### ❌ lxml Build Errors (macOS)

Fix:

```bash
pip install wheel
```

Then retry:

```bash
pip install -r requirements.txt
```

---

### ❌ Missing OpenAI API Key

Error:

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

### Contribution Flow

```text
Fork Repository
↓
Create Feature Branch
↓
Commit Changes
↓
Open Pull Request
```

---

## ⚖️ Ethical Usage

Use responsibly.

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

---

## 📜 License

MIT License