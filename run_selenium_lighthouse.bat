@echo off
echo [1] Starting dummy web server...
start /B cmd /C "npx serve -l 3000 > nul"

:: Wait a few seconds for server to boot
timeout /t 5 > nul

echo [2] Running Selenium test...
python test_selenium.py
IF %ERRORLEVEL% NEQ 0 (
    echo [x] Selenium test failed. Stopping.
    exit /b %ERRORLEVEL%
)

echo [3] Running Lighthouse audit...
python lighthouse-monitor-sub.py
IF %ERRORLEVEL% NEQ 0 (
    echo [x] Lighthouse audit failed.
    exit /b %ERRORLEVEL%
)

echo [4] Killing dummy server...
taskkill /f /im node.exe > nul 2>&1

echo [5] All done!
pause
