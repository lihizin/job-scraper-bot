import sqlite3
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import date
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# === CONFIG ===
chromedriver_path = "./chromedriver"
chrome_binary_path = "./Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"
sender_email = "jobboardlihi@gmail.com"
recipient_emails = ["lihi.zin@outlook.com", "uriel867@gmail.com"]

# Keywords
KEYWORDS = [ "junior", "entry level", "intern", "student", "graduate", "software engineer", "software developer",
    "backend developer", "frontend developer", "fullstack developer", "qa engineer", "qa automation",
    "data analyst", "devops","data","r&d intern", "security analyst", "platform engineer", "dotnet developer",
    "python developer", "c++ developer", "algorithm engineer", "prompt engineer", "data scientist"]

LOCATION_KEYWORDS = [
    "israel", "tel aviv", "herzliya", "jerusalem", "haifa", "beer sheva", "petah tikva",
    "ramat gan", "givatayim", "netanya", "hod hasharon", "raanana", "rehovot", "holon",
    "bat yam", "bnei brak", "yokneam", "ashdod", "ashkelon", "kfar saba", "modiin"
]

EXCLUDE_KEYWORDS = ["senior", "staff", "lead", "manager", "architect", "Senior"]

# === SETUP DRIVER ===
options = Options()
options.binary_location = chrome_binary_path
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

# === CONNECT TO DB ===
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()
cursor.execute("SELECT id, name, url FROM websites")
websites = cursor.fetchall()

matches = []

# === SCRAPE EACH WEBSITE ===
for website_id, name, url in websites:
    print(f"🔍 Checking: {name} - {url}")
    try:
        driver.get(url)
        time.sleep(10)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        job_elements = soup.find_all("a")
        print(f"Found {len(job_elements)} possible jobs")

        for job in job_elements:
            title = re.sub(r"\s+", " ", job.get_text().strip().lower())
            link = job.get("href", "#")

            # Skip very short text (likely not job titles)
            if len(title.strip()) < 10:
                continue

            if any(x in title for x in EXCLUDE_KEYWORDS):
                continue

            if any(k in title for k in KEYWORDS) and any(loc in title for loc in LOCATION_KEYWORDS):
                if link.startswith("/"):
                    link = url.rstrip("/") + link

                cursor.execute("""
                    INSERT OR IGNORE INTO job_posts (website_id, title, link, found_on)
                    VALUES (?, ?, ?, ?)
                """, (website_id, title, link, date.today()))

                matches.append(f"- {name}: {title}\n🔗 {link}")
                print(f"✅ Matched: {name} - {title}")

    except Exception as e:
        print(f"❌ Error checking {name}: {e}")

# === CLEANUP ===
conn.commit()
conn.close()
driver.quit()

# === SEND EMAIL ===
if matches:
    message = MIMEMultipart("alternative")
    message["Subject"] = f"{len(matches)} New Job Matches Found - {date.today()}"
    message["From"] = sender_email
    message["To"] = ", ".join(recipient_emails)

    body = "\U0001F9E0 Here are your matches for today:\n\n" + "\n\n".join(matches)
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, "your_app_password")  # Replace with app password
            server.sendmail(sender_email, recipient_emails, message.as_string())
        print("✉️ Email sent!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
else:
    print("❌ No new matches to email.")
