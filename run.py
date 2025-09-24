#!/usr/bin/env python3
"""
Launch script for YouTube Downloader
Handles dependency checking and provides helpful error messages
"""

import sys
import os
from pathlib import Path

def check_python_version():
    """Check if Python version is supported"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        print(f"   Current version: {sys.version}")
        return False
    return True

def check_dependencies():
    """Check if required dependencies are installed"""
    missing_deps = []
    
    try:
        import wx
    except ImportError:
        missing_deps.append("wxpython")
    
    try:
        import pytube
    except ImportError:
        missing_deps.append("pytube")
    
    try:
        import requests
    except ImportError:
        missing_deps.append("requests")
    
    if missing_deps:
        print("❌ Missing required dependencies:")
        for dep in missing_deps:
            print(f"   - {dep}")
        print("\nTo install missing dependencies, run:")
        print(f"   pip install {' '.join(missing_deps)}")
        print("\nOr install all dependencies with:")
        print("   pip install -r requirements.txt")
        return False
    
    return True

def main():
    """Main entry point with dependency checking"""
    print("YouTube Downloader - Starting...")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        return 1
    
    # Check dependencies
    if not check_dependencies():
        return 1
    
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Import and run the main application
    try:
        from youtube_downloader import main as app_main
        print("✅ All dependencies found")
        print("🚀 Starting YouTube Downloader...")
        app_main()
        return 0
        
    except Exception as e:
        print(f"❌ Error starting application: {str(e)}")
        print("\nIf you're on Linux, you might need to install additional packages:")
        print("   sudo apt-get install libgtk-3-dev libwebkitgtk-3.0-dev")
        print("\nOn macOS, ensure Xcode command line tools are installed:")
        print("   xcode-select --install")
        return 1

if __name__ == "__main__":
    sys.exit(main())