# AI Resume Parser Bot

## Overview

AI-powered Resume Parser Bot that automatically analyzes resumes uploaded through Telegram, extracts candidate information, calculates ATS scores, and stores data in Excel and SQL databases.

---

## Features

* Resume Upload via Telegram Bot
* PDF Resume Text Extraction
* AI-Powered Resume Analysis
* Skill Extraction
* ATS Score Calculation
* Excel Data Storage
* SQL Database Integration
* Automated Shortlisting

---

## Tech Stack

* Python
* Telegram Bot API
* Groq/OpenAI API
* SQL Database
* Excel (OpenPyXL)
* Git & GitHub

---

## Project Architecture

![Architecture](screenshots/architecture.png)

---

## Telegram Bot Output

![Bot Output](screenshots/bot_output.png)

---

## ATS Score Result

![ATS Score](screenshots/ats_score.png)

---

## Excel Storage

![Excel Data](screenshots/excel_data.png)

---

## Project Flow

Resume Upload → PDF Extraction → AI Analysis → ATS Score Calculation → Database Storage → Candidate Ranking → Shortlisting

---

## Installation

```bash
git clone https://github.com/Bhargavi2809/resume_parser.git
cd resume_parser
pip install -r requirements.txt
python telegram_bot.py
```

## Sample Output

```text
📄 RESUME ANALYSIS COMPLETE

👤 Name: Riya Talwar
📧 Email: riya.talwar@gmail.com
📱 Phone: 9876543210

✅ Matched: sql, excel, pandas, python, nlp, machine learning
❌ Missing: power bi

📊 Score: 86%
📌 Status: Strong Match
🎯 Shortlist: Shortlisted

## Future Enhancements

* Google Sheets Integration
* Interview Scheduling
* Email Notifications
* Resume Ranking Dashboard
* Web Application Interface
