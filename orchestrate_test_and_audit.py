import subprocess
import sys

try:
    print("[1] Running Selenium test...")
    subprocess.run(["python", "test_selenium.py"], check=True)

    print("[2] Running Lighthouse audits...")
    subprocess.run(["python", "lighthouse-monitor-sub.py"], check=True)

    print("[3] Orchestration completed.")

except subprocess.CalledProcessError as e:
    print(f"[x] Process failed: {e}")
    sys.exit(1)
