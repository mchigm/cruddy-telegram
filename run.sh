#!/bin/bash
# Shell script to run YouTube Downloader on Linux/macOS

echo "Starting YouTube Downloader..."

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    python3 run.py
elif command -v python &> /dev/null; then
    python run.py
else
    echo "Error: Python is not installed or not in PATH"
    exit 1
fi