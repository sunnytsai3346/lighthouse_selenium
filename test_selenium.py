from selenium import webdriver
import subprocess
import time

# Step 1: Start Selenium (Chrome) with remote debugging enabled
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--remote-debugging-port=9222")  # Required for Lighthouse
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

try:
    # Step 2: Navigate to dummy web app
    print("Opening dummy app...")
    driver.get("http://localhost:3000")
    time.sleep(5)  # Wait for page to load

    
   

finally:
    driver.quit()
