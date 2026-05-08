# 🎓 Academic Faculty Research Crawler

> AI-powered academic intelligence crawler for discovering professors, extracting research metadata, parsing CVs, identifying outreach-ready contacts, and generating ranked faculty datasets across top universities.

---

# 🚀 Features

## 🔍 Faculty Discovery
- Crawl university faculty directories
- Handle dynamic lazy-loaded pages
- Infinite scroll support
- Profile stabilization detection

---

## 🧠 AI Metadata Enrichment
Uses OpenAI models to:
- extract structured professor metadata,
- identify expertise,
- summarize research areas,
- standardize academic profiles.

---

## 📄 Deep CV & Resume Parsing

The crawler recursively explores:

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
- CV PDFs
- external websites
- academic bios
- personal homepages

---

## 📧 Advanced Email Extraction

Extracts emails from:
- faculty pages,
- mailto links,
- personal websites,
- PDF resumes,
- obfuscated HTML.

---

## 🏆 Faculty Relevance Scoring

Ranks professors based on relevance to:
- Product Management
- Strategy
- Innovation
- Behavioral Economics
- Organizational Behavior
- AI Systems
- Consumer Research
- Platform Strategy

---

## 🗂️ University-Specific Storage

Each university gets:
- dedicated SQLite database,
- dedicated CSV export.

---

# 🏗️ Project Architecture

```text
academic-research-crawler/
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

# 🏫 Supported Universities

Currently optimized for:
- Stanford GSB
- MIT Sloan
- Harvard Business School

Easily extensible to:
- Wharton
- Kellogg
- Booth
- Columbia
- Berkeley Haas
- Yale SOM
- INSEAD
- LBS
- UCLA Anderson

---

# ⚙️ Installation Guide

# 1️⃣ Clone Repository

```bash
git clone <your-repository-url>
```

Move into project:

```bash
cd academic-research-crawler
```

---

# 2️⃣ Create Virtual Environment

## 🍎 macOS / Linux

Create environment:

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 🪟 Windows

Create environment:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

# 3️⃣ Upgrade pip

```bash
pip install --upgrade pip
```

---

# 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 5️⃣ Install Playwright Browsers

```bash
playwright install
```

---

# 🔑 OpenAI API Setup

This project uses OpenAI APIs for:
- metadata extraction,
- expertise classification,
- research summarization,
- structured JSON generation.

---

# 6️⃣ Create `.env` File

Create a file named:

```text
.env
```

inside project root.

Add:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

# 🔐 Generate OpenAI API Key

Get your API key from:

https://platform.openai.com/api-keys

---

# ⚠️ Important API Notes

API usage depends on:
- your OpenAI billing plan,
- quota,
- rate limits,
- model availability.

This repository does NOT provide:
- bundled credits,
- shared API access,
- proxy APIs.

You are responsible for:
- your API billing,
- quota management,
- OpenAI policy compliance.

---

# ▶️ Running The Crawler

Start crawler:

```bash
python -m app.main
```

---

# 🏛️ University Selection

You will see:

```text
AVAILABLE UNIVERSITIES

1. Stanford Graduate School of Business
2. MIT Sloan
3. Harvard Business School
```

Enter:

```text
Enter university number:
```

Then confirm:

```text
Proceed with crawling? (yes/no):
```

---

# 🔄 Crawl Execution Flow

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

# 🌐 Stanford Lazy Loading Handling

Stanford dynamically loads faculty cards.

The crawler:
- scrolls repeatedly,
- waits 15 seconds after each scroll,
- finalizes only after profile stabilization.

This avoids:
- incomplete extraction,
- partial faculty discovery.

---

# 📬 Validation Rules

A professor record is valid only if:

## ✅ Required
- valid professor name
- valid email

## ➕

At least ONE of:
- department
- expertise
- research_interests

---

# 📧 Email Validation

The crawler automatically rejects:
- malformed emails,
- fake placeholders,
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

# 🚫 Duplicate Prevention

Duplicates are prevented using:
- faculty URLs,
- professor names,
- professor emails.

---

# 📊 Output Files

# 🗄️ SQLite Database

Example:

```text
stanford_graduate_school_of_business_professors.db
```

---

# 📄 CSV Export

Generated inside:

```text
data/exports/
```

Example:

```text
stanford_graduate_school_of_business_professors.csv
```

---

# 🧹 Database Utilities

# Remove Duplicate Records

```bash
python -m app.database.remove_duplicates
```

Removes duplicates using:
- email.

---

# Clear Database

```bash
python -m app.database.clear_db
```

This:
- deletes all records,
- preserves schema,
- asks for confirmation.

---

# 🛠️ Common Installation Issues

# ❌ Playwright Not Installed

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

# ❌ lxml Build Errors (macOS)

Fix:

```bash
pip install wheel
```

Then retry:

```bash
pip install -r requirements.txt
```

---

# ❌ Missing OpenAI API Key

Error:

```text
OPENAI_API_KEY not found
```

Fix:
- create `.env`,
- add valid API key.

---

# 💻 Recommended Environment

Recommended:
- Python 3.10+
- macOS / Linux
- VSCode
- SQLite Browser

---

# 🧰 Technologies Used

- Python
- Playwright
- BeautifulSoup
- Requests
- SQLAlchemy
- SQLite
- OpenAI API
- Pandas

---

# 🚀 Recommended Future Enhancements

Potential upgrades:
- async crawling,
- proxy rotation,
- retry queues,
- Redis caching,
- semantic vector search,
- publication extraction,
- research-paper scoring,
- embeddings-based ranking,
- automated outreach generation,
- multi-university orchestration.

---

# 🤝 Open For Contributions

Contributions are welcome.

Areas where contributions would help:
- support for more universities,
- async crawling architecture,
- publication extraction,
- semantic search,
- faculty recommendation systems,
- outreach automation,
- retry pipelines,
- proxy support,
- ranking improvements,
- UI dashboard.

If you'd like to contribute:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---

# ⚖️ Ethical Usage

Use responsibly.

❌ Do NOT:
- spam professors,
- misuse extracted emails,
- violate university policies,
- aggressively scrape protected systems.

✅ Recommended use:
- academic networking,
- research collaboration,
- internship discovery,
- educational outreach.

---

# 📜 License

MIT License