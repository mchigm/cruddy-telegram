#!/usr/bin/env python3
"""
Test script for core YouTube downloading functionality
This tests the core features without requiring GUI components
"""

import os
import sys
from pathlib import Path
from pytube import YouTube
import requests

def test_pytube_functionality():
    """Test if pytube can access YouTube videos"""
    print("Testing pytube functionality...")
    
    # Test with a known public video (example)
    test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Rick Roll - always available for testing
    
    try:
        yt = YouTube(test_url)
        print(f"✅ Successfully accessed video: {yt.title}")
        print(f"   Duration: {yt.length} seconds")
        print(f"   Views: {yt.views}")
        
        # Get available streams
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        print(f"   Available progressive MP4 streams: {len(streams)}")
        
        if streams:
            best_stream = streams.order_by('resolution').desc().first()
            print(f"   Best quality: {best_stream.resolution} ({best_stream.filesize} bytes)")
        
        return True
        
    except Exception as e:
        print(f"❌ Error accessing YouTube: {str(e)}")
        return False

def test_downloads_directory():
    """Test downloads directory creation"""
    print("\nTesting downloads directory...")
    
    downloads_dir = Path("downloads")
    downloads_dir.mkdir(exist_ok=True)
    
    if downloads_dir.exists() and downloads_dir.is_dir():
        print("✅ Downloads directory created successfully")
        return True
    else:
        print("❌ Failed to create downloads directory")
        return False

def test_requests_functionality():
    """Test requests library for network connectivity"""
    print("\nTesting network connectivity...")
    
    try:
        response = requests.get("https://www.youtube.com", timeout=10)
        if response.status_code == 200:
            print("✅ Successfully connected to YouTube")
            return True
        else:
            print(f"⚠️  YouTube returned status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Network error: {str(e)}")
        return False

def test_file_operations():
    """Test basic file operations for video management"""
    print("\nTesting file operations...")
    
    test_file = Path("downloads/test_file.txt")
    test_file.parent.mkdir(exist_ok=True)
    
    try:
        # Write test file
        test_file.write_text("Test content")
        
        # Read test file
        content = test_file.read_text()
        
        # Check size
        size = test_file.stat().st_size
        
        # Delete test file
        test_file.unlink()
        
        print("✅ File operations working correctly")
        return True
        
    except Exception as e:
        print(f"❌ File operation error: {str(e)}")
        return False

def main():
    """Run all tests"""
    print("YouTube Downloader - Core Functionality Tests")
    print("=" * 50)
    
    tests = [
        test_downloads_directory,
        test_file_operations,
        test_requests_functionality,
        test_pytube_functionality,
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 50)
    print("Test Results:")
    passed = sum(results)
    total = len(results)
    print(f"✅ Passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All core functionality tests passed!")
        print("The application should work correctly when GUI components are available.")
    else:
        print("⚠️  Some tests failed. Please check the issues above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)