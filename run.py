import subprocess
import sys
import os

# Detect virtual environment Python path
venv_python = os.path.join("venv", "bin", "python") if os.name != "nt" else os.path.join("venv", "Scripts", "python.exe")

if not os.path.exists(venv_python):
    print("❌ Virtual environment not found. Please create it with: python3 -m venv venv")
    sys.exit(1)

# Run scraper
print("🚀 Running scraper.py...")
subprocess.run([venv_python, "scraper.py"], check=True)

# Run email sender
print("📧 Running email_jobs.py...")
subprocess.run([venv_python, "email_jobs.py"], check=True)
