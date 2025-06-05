import sqlite3
import smtplib
import os
from datetime import date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# === LOAD ENV VARIABLES ===
load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAILS = os.getenv("TO_EMAILS").split(",")

# === CONNECT TO DB ===
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()
today = date.today()
cursor.execute("SELECT title, link FROM job_posts WHERE found_on = ?", (today,))
jobs = cursor.fetchall()
conn.close()

# === CHECK IF THERE ARE JOBS ===
if not jobs:
    print("📭 No new jobs today – no email sent.")
    exit()

# === BUILD EMAIL CONTENT ===
subject = f"{len(jobs)} New Job Matches Found – {today}"
body = "🧠 Here are your matches for today:\n\n"
for title, link in jobs:
    body += f"- {title}\n  🔗 {link}\n\n"

# === CREATE EMAIL ===
msg = MIMEMultipart()
msg['From'] = EMAIL_ADDRESS
msg['To'] = ", ".join(TO_EMAILS)
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# === SEND EMAIL ===
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, TO_EMAILS, msg.as_string())
    print(f"✅ Email sent to: {', '.join(TO_EMAILS)} with {len(jobs)} jobs.")
except Exception as e:
    print(f"❌ Failed to send email: {e}")
