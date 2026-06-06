import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="resume_screening_db",
    user="postgres",
    password="Bhargavi@123"
)

print("Database Connected Successfully")
print("PYTHON IS WORKING")