import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def analyze_resume(text):

    if not GROQ_API_KEY:
        print("❌ GROQ_API_KEY not found in .env")
        return {"name": "Unknown", "skills": [], "experience": 0}

    prompt = f"""
Extract information from resume and return ONLY valid JSON.

Format:
{{
    "name": "",
    "skills": [],
    "experience": 0
}}

Rules:
- Return ONLY JSON
- experience must be number
- skills must be list
- name must be string

Resume:
{text}
"""

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama3-70b-8192",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0
            },
            timeout=30
        )

        if response.status_code != 200:
            print("❌ API Error:", response.text)
            return {"name": "Unknown", "skills": [], "experience": 0}

        result = response.json()

        content = result.get("choices", [{}])[0].get("message", {}).get("content", "")

        if not content:
            print("❌ Empty response from AI")
            return {"name": "Unknown", "skills": [], "experience": 0}

        content = content.replace("```json", "").replace("```", "").strip()

        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            print("❌ JSON parsing failed:", content)
            return {"name": "Unknown", "skills": [], "experience": 0}

        return {
            "name": data.get("name", "Unknown"),
            "skills": data.get("skills", []),
            "experience": data.get("experience", 0)
        }

    except Exception as e:
        print("❌ AI Analyzer Error:", e)

        return {"name": "Unknown", "skills": [], "experience": 0}