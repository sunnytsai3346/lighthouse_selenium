import subprocess

url = "http://localhost:3000"  # Change to your actual target
report_path ="./lighthouse-report-1.json"

print(f"Auditing {url}...")
NPX_CMD = r"C:\\nvm4w\\nodejs\\npx.cmd"   #where npx
subprocess.run([
    NPX_CMD, "lighthouse",
    url,
    "--port=9222",
    "--output=json",
    f"--output-path={report_path}",
    "--quiet"
], check=True)

print(f"Lighthouse report saved to {report_path}")
