import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def save_candidate(name, email, phone, matched, missing, score, status):

    conn = None
    cur = None

    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

        cur = conn.cursor()

        cur.execute("""
            INSERT INTO candidates (
                name,
                email,
                phone,
                matched_skills,
                missing_skills,
                score,
                status
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            name,
            email,
            phone,
            ",".join(matched or []),
            ",".join(missing or []),
            score,
            status
        ))

        conn.commit()
        print("✅ Data saved to database")

    except Exception as e:
        print("❌ DB ERROR:", e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()