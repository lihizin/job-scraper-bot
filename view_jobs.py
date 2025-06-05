import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

cursor.execute("""
SELECT job_posts.id, websites.name, title, link, found_on, notified
FROM job_posts
JOIN websites ON job_posts.website_id = websites.id
ORDER BY found_on DESC
""")

rows = cursor.fetchall()

if not rows:
    print("😕 No matching jobs were found yet.")
else:
    print("✅ Jobs found:\n")
    for row in rows:
        print(f"🧩 {row[1]} - {row[2]}")
        print(f"🔗 {row[3]}")
        print(f"📅 Found on: {row[4]} | Notified: {row[5]}\n")

conn.close()
