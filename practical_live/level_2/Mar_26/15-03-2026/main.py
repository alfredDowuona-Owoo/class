import os
from dotenv import load_dotenv
import psycopg2

# Load the variables
load_dotenv()

try:
    # Connect using variables from .env
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )
    print("Connection successful!")
    conn.close()
except Exception as e:
    print(f"Error: {e}")