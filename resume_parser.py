import re
import pdfplumber


# ================= TEXT EXTRACTION =================


def extract_text(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
             text += page.extract_text().lower()
    return text

def extract_name(text):
    lines = text.split("\n")

    for line in lines[:10]:  # check only top part
        line = line.strip()

        # skip empty or email/phone lines
        if "@" in line or any(char.isdigit() for char in line):
            continue

        # basic name condition (2-4 words, alphabets only)
        words = line.split()
        if 1 < len(words) <= 4 and all(w.isalpha() for w in words):
            return line

    return "Unknown"

# ================= SKILL EXTRACTION =================
def extract_text(path):

    text = ""

    with pdfplumber.open(path) as pdf:

        for page in pdf.pages:

            t = page.extract_text()

            if t:
                text += t

    return text

# ================= CONTACT EXTRACTION =================


def extract_contact_details(text):
    # EMAIL
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    emails = re.findall(email_pattern, text)

    # PHONE (India + international safe format)
    phone_pattern = r'(\+91[-\s]?)?[6-9]\d{9}'

    phones = re.findall(phone_pattern, text)

    # 🔥 FIX: re-find full number properly
    phone_full_pattern = r'(?:\+91[-\s]?)?[6-9]\d{9}'
    full_phones = re.findall(phone_full_pattern, text)

    email = emails[0] if emails else "Not Found"
    phone = full_phones[0] if full_phones else "Not Found"

    return email, phone