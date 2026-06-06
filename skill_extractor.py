import re

SKILLS_DB = [
    "python",
    "sql",
    "excel",
    "power bi",
    "machine learning",
    "pandas",
    "numpy"
]

def extract_skills(text):

    if not text:
        return []

    text = text.lower()
    found = []

    for skill in SKILLS_DB:

        pattern = r'\b' + re.escape(skill) + r'\b'

        if re.search(pattern, text):
            found.append(skill)

    return found