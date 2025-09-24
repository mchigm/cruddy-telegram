@echo off
REM Windows batch script to run YouTube Downloader
echo Starting YouTube Downloader...
python run.py
if errorlevel 1 (
    echo.
    echo Press any key to exit...
    pause >nul
)