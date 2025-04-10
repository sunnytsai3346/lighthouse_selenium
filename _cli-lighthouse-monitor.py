import subprocess
import threading
import time
import os

LIGHTHOUSE_CLI = "lhci"
URLS_TO_MONITOR = [
    "http://localhost:3000",  # Update this with the actual URLs you want to monitor
    "http://localhost:3000/dashboard",  # Example: a page you know will be tested
]

RUN_DURATION = 120  # Monitor for 2 minutes or match Selenium test runtime

# Function to run Lighthouse CI (`lhci autorun`)
def run_lhci_monitor():
    print("🚀 Running Lighthouse CI monitor")
    subprocess.run([LIGHTHOUSE_CLI, "autorun", "--config=lighthouserc.js"])

# Function to simulate waiting for the Selenium test to finish
def wait_for_selenium_test():
    print("⏳ Waiting for Selenium test to complete...")
    time.sleep(RUN_DURATION)  # Simulate wait (you can adjust this)

# Main function that coordinates everything
def main():
    # Start Lighthouse CI monitor in a background thread
    monitor_thread = threading.Thread(target=run_lhci_monitor)
    monitor_thread.start()

    # Start waiting for Selenium test to finish (simulate or call your actual Selenium test here)
    wait_for_selenium_test()

    # Ensure monitor thread finishes before the script ends
    monitor_thread.join()
    print("✅ Lighthouse CI completed and reports uploaded.")

if __name__ == "__main__":
    main()
