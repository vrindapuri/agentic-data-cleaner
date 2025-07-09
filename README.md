# 🧠 Agentic Data Cleaner

An intelligent, modular data-cleaning pipeline built using a lightweight **agentic system**. This project simulates how independent agents can collaborate to detect, correct, and enrich messy customer data — powered by traditional heuristics and LLMs (Gemini).

---

## 💼 Problem Statement

Real-world datasets are rarely clean. They come with:
- Missing fields
- Typos
- Invalid formats (e.g., emails)
- Duplicates
- Incomplete or inconsistent labels

We address this by simulating **autonomous agents** that work in a pipeline — from raw ingestion to enriched output.

---

## 🔁 Agentic Workflow

Each agent performs a dedicated task:

### 1️⃣ Detection Agent
- Detects:
  - Missing fields (name, email, etc.)
  - Invalid emails (non-standard format)
  - Invalid industry values (e.g., misspelled)
  - Duplicates
- Logs all issues to `logs/detection_log.txt`

### 2️⃣ Correction Agent
- Fixes:
  - Standardizes capitalization
  - Removes duplicates
  - Uses fuzzy matching to correct invalid industry names
- Logs all fixes to `logs/correction_log.txt`

### 3️⃣ Enrichment Agent (Gemini LLM)
- Uses Google Gemini API to:
  - Fill missing values (e.g., missing name/spend) based on row context
- Logs enriched fields to `logs/enrichment_log.txt`

### 4️⃣ UI Agent (Optional)
- Built with **Streamlit**
- Lets users:
  - Upload a messy CSV
  - View cleaned data
  - Download final output

---

## 📂 Project Structure

```bash
agentic_data_cleaner/
│
├── agents/
│   ├── detection_agent.py
│   ├── correction_agent.py
│   └── enrichment_agent.py
│
├── data/
│   ├── test_customers_50rows.csv   # Sample input
│   └── final_enriched.csv          # Final output
│
├── logs/
│   ├── detection_log.txt
│   ├── correction_log.txt
│   └── enrichment_log.txt
│
├── main.py
├── ui_agent.py
├── requirements.txt
└── README.md

