import subprocess


with open("visited_urls.txt") as f:
    urls = [line.strip() for line in f if line.strip()]

#url = "http://localhost:3000"  # Change to your actual target
#report_path ="./lighthouse-report-1.json"
for url in urls:
    print(f"Auditing {url}...")
    slug = url.replace("http://", "").replace("/", "_").strip("_")
    output_path = f".\lighthouse_report\lighthouse-report-{slug}.json"
    NPX_CMD = r"C:\\nvm4w\\nodejs\\npx.cmd"   #where npx
    subprocess.run([
        NPX_CMD, "lighthouse",
        url,
        "--port=9222",
        "--output=json",
        "--form-factor=mobile",
        "--screenEmulation.width=360",
        "--screenEmulation.height=640",
        "--output=html",
        f"--output-path={output_path.replace('.json', '')}",
        "--quiet"
    ], check=True)

print(f"Lighthouse report saved lighthouse_report directory")
