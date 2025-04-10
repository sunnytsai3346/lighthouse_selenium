### selenium and lighthouse together ###
- run test_lighthouse_selenium.py to generate lighthouse.json
### selenium and lighthouse are exectured seperately ###
- option 1 (not good) . know the path [] that selenium will go over , and run lighthouse-monitor to generate lighthouse.json
- option 2.  run_selenium_lighthouse.bat . will run test_selenium.py first , and run lighthouse-monitor-sub.py to generate lighthouse-1.json (report)
### how to read lighthouse.json 
- https://googlechrome.github.io/lighthouse/viewer/
