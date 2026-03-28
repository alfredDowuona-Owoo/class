import sqlite3
import os

DB_PATH = os.path.join("data", "documents.db")


#get connection to database
def get_connection():
    return sqlite3.connect(str(DB_PATH))


## create schema
def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    #document table
    cursor.execute("""
                            CREATE TABLE IF NOT EXISTs documents (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            path TEXT,
                            thumbnail_path TEXT,
                            tags TEXT,
                            description TEXT,
                            upload_date TEXT,
                            lecture_date TEXT,
                            total_pages INTEGER      
    )               
    """)
    print("Database Initialized/Operation Successful.")
    conn.commit()
    conn.close()
