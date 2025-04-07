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
    time.sleep(3)  # Wait for page to load

    # Step 3: Run Lighthouse on the current URL
    target_url = driver.current_url
    print(f"Running Lighthouse on {target_url}")
    NPX_CMD = r"C:\\nvm4w\\nodejs\\npx.cmd"   #where npx
    

    subprocess.run([
        NPX_CMD, "lighthouse",
        target_url,
        "--port=9222",
        "--output=json",
        "--output-path=./lighthouse-report.json",
        #"--only-categories=performance"
        #"--quiet"
    ])

    
    print("Lighthouse report saved to lighthouse-report.json")

finally:
    driver.quit()
