import time
import requests
import subprocess
import os

TARGET_URL = "http://localhost:3000"
LIGHTHOUSE_PATH = os.path.expanduser(r"C:\\nvm4w\\nodejs\\npx.cmd")  # Or use 'npx' if PATH is set
URLS_TO_MONITOR = [
    "http://localhost:3000",           # homepage
    "http://localhost:3000/dashboard", # example page
    # Add more pages you expect Selenium to visit
]

RUN_DURATION = 120  # Monitor for 2 minutes or match Selenium test runtime


def run_lighthouse_loop():
    start_time = time.time()
    i = 0
    while time.time() - start_time < RUN_DURATION:
        for url in URLS_TO_MONITOR:
            out_path = f"lighthouse-report-{i}.json"
            print(f"📊 Running Lighthouse on {url} -> {out_path}")
            subprocess.run([
                LIGHTHOUSE_PATH, "lighthouse",
                url,
                "--port=9222",
                "--output=json",
                f"--output-path={out_path}",
                "--quiet"
            ])
            time.sleep(5)  # slight delay between audits
            i += 1

if __name__ == "__main__":
    run_lighthouse_loop()

# def wait_for_site(url, timeout=60):
#     print(f"⏳ Waiting for {url} to be available...")
#     for _ in range(timeout):
#         try:
#             r = requests.get(url)
#             if r.status_code == 200:
#                 print("✅ Site is up!")
#                 return True
#         except requests.exceptions.ConnectionError:
#             pass
#         time.sleep(1)
#     raise TimeoutError(f"❌ Timed out waiting for {url}")

# def run_lighthouse(url):
#     print(f"🚀 Running Lighthouse audit on {url}")
#     subprocess.run([
#         LIGHTHOUSE_PATH, "lighthouse",
#         url,
#         "--port=9222",
#         "--output=json",
#         "--output-path=lighthouse-report.json",
#         "--quiet"
#     ])
#     print("✅ Lighthouse report saved to lighthouse-report.json")

# if __name__ == "__main__":
#     wait_for_site(TARGET_URL)
#     run_lighthouse(TARGET_URL)
