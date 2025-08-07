#### lighthouse_selenium (Performance auditing using Selenium & Lighthouse) ####
Description:
Automated tool that runs Google Lighthouse audits on pages using Selenium for performance, accessibility, best practices with possible integration into CI pipelines.

README Sections:

⚙️ Overview — automated Lighthouse tests via Selenium browser automation.

📚 Tech Stack — Selenium WebDriver, Node.js or Python, Lighthouse CLI.

🔍 Functionality — run audits, save JSON/html reports, aggregate metrics.

🔁 Getting Started — dependency install, setup, run test script/tab.

📊 Sample Report — include excerpts of lighthouse scores.

🧪 ** CI/CD Integration** — example pipeline script or GitHub Action template.

📝 Future Enhancements — thresholds-based CI fail, chart dashboards, Slack notifications.
---------

### selenium and lighthouse together ###
- run test_lighthouse_selenium.py to generate lighthouse.json
### selenium and lighthouse are exectured seperately ###
- option 1 (not good) . know the path [] that selenium will go over , and run lighthouse-monitor to generate lighthouse.json
- option 2.  run_selenium_lighthouse.bat . will run test_selenium.py first , and run lighthouse-monitor-sub.py to generate lighthouse-1.json (report)
- option 3. orchestrate_test_and_audit.py , run subprocess(test_selenium.py) , then subprocess(lighthouse-monitor-sub.py) , this can be used in linux
### how to read lighthouse.json 
- https://googlechrome.github.io/lighthouse/viewer/
