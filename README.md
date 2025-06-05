# 🧠 Job Scraper Bot
This project is a Python-based web scraper that collects job postings from multiple tech company career pages in Israel.  
It stores job data in a SQLite database and sends daily email alerts with newly found listings.
🧡 I created this bot to help my boyfriend, Uriel, find junior tech jobs more easily — automating the daily grind of browsing career pages.  
👨‍💻 Uriel is now actively contributing to the project by adding functionality for job application submission directly from the platform.

## 🚀 Features
- Scrapes job postings from dozens of Israeli tech companies
- Stores data in a local `SQLite` database
- Sends daily email summaries with matching jobs
- Uses `Selenium` for dynamic websites
- Easy to extend with new companies
---
## 🛠 Technologies
- Python 3
- Selenium & ChromeDriver
- SQLite
- smtplib (Email sending)
- Flask (for optional web view)
- dotenv (for managing environment variables)
---
## 📁 Project Structure
<pre><code>```text job-scraper-bot/ ├── scraper.py # Scraper logic ├── email_jobs.py # Email notification logic ├── add_websites.py # Script to populate the database with company URLs ├── db_setup.py # Initial database creation ├── app.py # Flask app (optional web view) ├── run.py # Main script to run everything ├── templates/ │ └── jobs.html # HTML template for job viewing ├── .env # Environment variables (email credentials etc.) ├── .gitignore # Git ignore rules └── README.md # You're here! ``` </code></pre>
