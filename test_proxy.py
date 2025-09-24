#!/usr/bin/env python3
"""
Simple proxy test script for YouTube Downloader
Run this to verify your proxy configuration is working
"""

import sys
import requests
from config import get_proxy_config, get_custom_headers, ENABLE_PROXY, PROXY_URL

def test_basic_connectivity():
    """Test basic internet connectivity"""
    print("Testing basic internet connectivity...")
    try:
        response = requests.get("https://httpbin.org/ip", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Basic connectivity OK - Your IP: {data.get('origin', 'Unknown')}")
            return True
        else:
            print(f"❌ Basic connectivity failed: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Basic connectivity failed: {e}")
        return False

def test_proxy_configuration():
    """Test proxy configuration"""
    print("\nTesting proxy configuration...")
    
    if not ENABLE_PROXY:
        print("ℹ️  Proxy is disabled (ENABLE_PROXY=False)")
        return True
    
    if not PROXY_URL:
        print("❌ Proxy enabled but PROXY_URL is not set")
        return False
    
    proxy_config = get_proxy_config()
    if not proxy_config:
        print("❌ Failed to generate proxy configuration")
        return False
    
    print(f"✅ Proxy URL configured: {PROXY_URL}")
    print(f"✅ Proxy config generated: {list(proxy_config.keys())}")
    
    # Test proxy connectivity
    try:
        print("Testing proxy connectivity...")
        session = requests.Session()
        session.headers.update(get_custom_headers())
        session.proxies.update(proxy_config)
        
        response = session.get("https://httpbin.org/ip", timeout=15)
        if response.status_code == 200:
            data = response.json()
            proxy_ip = data.get('origin', 'Unknown')
            print(f"✅ Proxy connectivity OK - Proxy IP: {proxy_ip}")
            return True
        else:
            print(f"❌ Proxy connectivity failed: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Proxy connectivity failed: {e}")
        return False

def test_youtube_access():
    """Test YouTube access with current configuration"""
    print("\nTesting YouTube access...")
    
    try:
        session = requests.Session()
        session.headers.update(get_custom_headers())
        
        proxy_config = get_proxy_config()
        if proxy_config:
            session.proxies.update(proxy_config)
            print("Using proxy for YouTube test...")
        
        # Test accessing YouTube main page
        response = session.get("https://www.youtube.com", timeout=15)
        if response.status_code == 200:
            print("✅ YouTube access OK")
            return True
        else:
            print(f"❌ YouTube access failed: HTTP {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ YouTube access failed: {e}")
        return False

def main():
    """Run all proxy tests"""
    print("YouTube Downloader - Proxy Configuration Test")
    print("=" * 50)
    
    tests = [
        ("Basic Connectivity", test_basic_connectivity),
        ("Proxy Configuration", test_proxy_configuration),
        ("YouTube Access", test_youtube_access),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n[{test_name}]")
        result = test_func()
        results.append(result)
    
    print("\n" + "=" * 50)
    print("Test Results Summary:")
    passed = sum(results)
    total = len(results)
    
    for i, (test_name, _) in enumerate(tests):
        status = "✅ PASS" if results[i] else "❌ FAIL"
        print(f"  {test_name}: {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your configuration should work for downloading.")
    else:
        print("⚠️  Some tests failed. Check the configuration:")
        print("   - Verify your proxy server is working")
        print("   - Check proxy URL format in config.py")
        print("   - Try a different proxy server")
        print("   - Consider using a VPN instead")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)