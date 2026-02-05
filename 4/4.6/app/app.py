from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Параметри підключення до PostgreSQL з Docker Compose
DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_NAME = os.getenv("POSTGRES_DB", "testdb")
DB_USER = os.getenv("POSTGRES_USER", "user")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "password")

@app.route("/")
def index():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()
        return f"PostgreSQL version: {version[0]}"
    except Exception as e:
        return f"Cannot connect to DB: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)