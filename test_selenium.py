from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
import sys

# Step 1: Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--remote-debugging-port=9222")  # Required for Lighthouse
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

visited_urls = [] # this is for lighthouse

try:
    # Step 2: Start WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        print("[**] Opening dummy app...")
        driver.get("http://localhost:3000")
        visited_urls.append(driver.current_url)  ## need selenium to add driver.current_url to visited_urls
        time.sleep(5)  # Wait for page to load


        # driver.get("http://localhost:3000/profile")
        # visited_urls.append(driver.current_url)
        # time.sleep(3)

        # You can add further actions/assertions here
        print("[**] Selenium test completed successfully.")

    finally:
        driver.quit()
        # Save to file
        with open("visited_urls.txt", "w") as f:
            for url in visited_urls:
                f.write(url + "\n")

except WebDriverException as e:
    print(f"[❌] Selenium test failed. Stopping.\nError: {e}")
    sys.exit(1)
