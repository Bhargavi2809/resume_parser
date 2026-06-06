import os
import re
import pdfplumber
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

from excel_sheet import save_to_excel
from database import save_candidate

# ================= LOAD ENV =================
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ================= CONFIG =================
RESUME_DIR = "resumes"
os.makedirs(RESUME_DIR, exist_ok=True)

SKILL_DB = {"python", "sql", "excel", "pandas", "machine learning", "nlp", "power bi"}

# ================= TEXT EXTRACTION =================
def extract_text(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text.lower()

# ================= EXTRACT DETAILS =================
def extract_email(text):
    match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return match.group() if match else "Not Found"

def extract_phone(text):
    match = re.search(r"(\+?\d{1,3}[- ]?)?\d{10}", text)
    return match.group() if match else "Not Found"

def extract_name(text):
    lines = text.split("\n")
    for line in lines[:20]:
        if line and "@" not in line and not any(i.isdigit() for i in line):
            if 2 <= len(line.split()) <= 4:
                return line.title()
    return "Not Found"

# ================= SKILLS =================
def extract_skills(text):
    found = [skill for skill in SKILL_DB if skill in text]
    missing = list(SKILL_DB - set(found))
    return found, missing

def calculate_score(found):
    return (len(found) / len(SKILL_DB)) * 100

# ================= HANDLER =================
async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):

    document = update.message.document
    file = await context.bot.get_file(document.file_id)

    file_path = os.path.join(RESUME_DIR, f"{document.file_id}.pdf")
    await file.download_to_drive(file_path)

    text = extract_text(file_path)

    name = extract_name(text)
    email = extract_email(text)
    phone = extract_phone(text)

    matched, missing = extract_skills(text)
    score = calculate_score(matched)

    if score >= 70:
        status = "Shortlisted"
        match_type = "Strong Match"
    elif score >= 40:
        status = "Not Shortlisted"
        match_type = "Moderate Match"
    else:
        status = "Not Shortlisted"
        match_type = "Weak Match"

    save_to_excel(name, email, phone, matched, missing, score, status)

    save_candidate(name, email, phone, matched, missing, score, status)

    await update.message.reply_text(f"""
📄 RESUME ANALYSIS COMPLETE

👤 Name: {name}
📧 Email: {email}
📱 Phone: {phone}

✅ Matched: {', '.join(matched) if matched else 'None'}
❌ Missing: {', '.join(missing) if missing else 'None'}

📊 Score: {score:.0f}%
📌 Status: {match_type}
🎯 Shortlist: {status}
""")

# ================= START =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send your resume PDF")

# ================= MAIN =================
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_document))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()