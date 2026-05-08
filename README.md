# Academic Intelligence Engine

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT4.1-green?style=for-the-badge&logo=openai)
![Playwright](https://img.shields.io/badge/Playwright-Crawler-purple?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-DB-orange?style=for-the-badge&logo=sqlite)
![MIT](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)

</div>

Academic Intelligence Engine is an AI-powered academic crawler that discovers professors across top universities, extracts research metadata, parses CVs and personal websites, identifies outreach-ready contacts, and generates ranked datasets for research collaboration and internship discovery.

---

## Overview

The engine recursively crawls faculty directories, professor profiles, personal websites, and CV PDFs to extract structured information such as emails, expertise, research interests, LinkedIn profiles, Google Scholar links, and faculty summaries. OpenAI models are used to standardize metadata and enrich academic profiles.

---

## Features

The crawler supports dynamic faculty discovery with lazy-loading and infinite scroll handling. It performs recursive crawling into external personal websites and CV PDFs to improve email extraction coverage. The system validates records, removes duplicates, ranks professors based on research relevance, and exports university-specific SQLite databases and CSV datasets.

---

## Architecture

```text
academic-intelligence-engine/
│
├── app/
│   ├── crawler/
│   ├── enrichment/
│   ├── database/
│   └── main.py
│
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

Clone the repository and move into the project directory.

```bash
git clone <your-repository-url>
cd academic-intelligence-engine
```

Create and activate a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies and Playwright browsers.

```bash
pip install -r requirements.txt
playwright install
```

Create a `.env` file in the project root and add your OpenAI API key.

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Generate API key from:

https://platform.openai.com/api-keys

---

## Running The Crawler

Start the crawler using:

```bash
python -m app.main
```

The crawler prompts for university selection and automatically processes faculty pages, personal websites, and CVs before generating ranked exports.

---

## Validation

A professor record is considered valid only if it contains a valid name, valid email, and at least one among department, expertise, or research interests. Invalid emails, malformed records, and duplicates are automatically rejected.

---

## Output

The engine generates university-specific SQLite databases and CSV exports containing structured faculty intelligence data.

Example outputs:

```text
stanford_graduate_school_of_business_professors.db
stanford_graduate_school_of_business_professors.csv
```

---

## Stack

The project uses Python, Playwright, BeautifulSoup, Requests, SQLAlchemy, SQLite, Pandas, and OpenAI APIs.

---

## Contributions

Contributions are welcome for extending university support, improving crawling performance, publication extraction, semantic search, ranking systems, and outreach automation.

---

## Usage

Use responsibly for academic networking, research collaboration, and internship discovery. Do not misuse extracted contact information or violate university usage policies.

---

MIT License
