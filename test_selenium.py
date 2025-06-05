from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# ✅ Correct paths (update if needed)
chromedriver_path = "./chromedriver"
chrome_binary_path = "./Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"

# ✅ Set Chrome options
options = Options()
options.binary_location = chrome_binary_path

# ✅ Set up ChromeDriver service
service = Service(executable_path=chromedriver_path)

# ✅ Launch the browser
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com")
time.sleep(3)
print("✅ Chrome opened successfully!")

driver.quit()
