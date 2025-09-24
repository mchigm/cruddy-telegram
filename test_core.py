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
from config import get_proxy_config, get_custom_headers

def test_geo_restriction_bypass():
    """Test geo-restriction bypass functionality"""
    print("Testing geo-restriction bypass functionality...")
    
    try:
        # Test proxy configuration
        proxy_config = get_proxy_config()
        if proxy_config:
            print(f"✅ Proxy configuration loaded: {list(proxy_config.keys())}")
        else:
            print("ℹ️  No proxy configuration (ENABLE_PROXY=False)")
        
        # Test custom headers
        headers = get_custom_headers()
        print(f"✅ Custom headers configured: {len(headers)} headers")
        print(f"   User-Agent: {headers.get('User-Agent', 'Not set')[:50]}...")
        
        # Test if requests can be made with custom headers
        test_session = requests.Session()
        test_session.headers.update(headers)
        if proxy_config:
            test_session.proxies.update(proxy_config)
        
        # Make a simple request to test connectivity
        response = test_session.get("https://httpbin.org/headers", timeout=10)
        if response.status_code == 200:
            print("✅ Enhanced session working correctly")
            return True
        else:
            print(f"❌ Enhanced session test failed: {response.status_code}")
            return False
        
    except Exception as e:
        print(f"❌ Error testing geo-restriction bypass: {str(e)}")
        return False

def test_pytube_functionality():
    """Test if pytube can access YouTube videos"""
    print("Testing pytube functionality...")
    
    # Test with a known public video (example)
    test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Rick Roll - always available for testing
    
    try:
        yt = YouTube(test_url)
        
        # Try to apply geo-restriction bypass settings
        try:
            if hasattr(yt, '_session'):
                custom_headers = get_custom_headers()
                yt._session.headers.update(custom_headers)
                proxy_config = get_proxy_config()
                if proxy_config:
                    yt._session.proxies.update(proxy_config)
                    print("✅ Applied proxy configuration for testing")
        except Exception as session_error:
            print(f"Note: Could not modify session: {session_error}")
        
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
        test_geo_restriction_bypass,
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