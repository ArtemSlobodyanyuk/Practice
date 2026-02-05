import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_URL")
API_KEY = os.getenv("API_KEY")

print("DB_URL:", DB_URL)
print("API_KEY:", API_KEY)