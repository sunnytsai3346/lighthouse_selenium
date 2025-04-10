from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
import sys

# Step 1: Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--remote-debugging-port=9222")  # Required for Lighthouse
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

try:
    # Step 2: Start WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        print("[**] Opening dummy app...")
        driver.get("http://localhost:3000")
        time.sleep(5)  # Wait for page to load

        # You can add further actions/assertions here
        print("[**] Selenium test completed successfully.")

    finally:
        driver.quit()

except WebDriverException as e:
    print(f"[❌] Selenium test failed. Stopping.\nError: {e}")
    sys.exit(1)
