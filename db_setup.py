# This script sets up SQLite database, with two tables:
# websites - stores the list of companies and their career page URLs
# job_posts - stores job listings found on those sites

import sqlite3

# Connect (creates the file if it doesn't exist)
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# Creating an empty table for tracking websites
cursor.execute("""
CREATE TABLE IF NOT EXISTS websites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    url TEXT NOT NULL
)
""")

# Creating an empty table for job posts
cursor.execute("""
CREATE TABLE IF NOT EXISTS job_posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    website_id INTEGER,
    title TEXT,
    link TEXT,
    found_on DATE,
    notified BOOLEAN DEFAULT 0,
    UNIQUE(title, link)
)
""")

conn.commit()
conn.close()