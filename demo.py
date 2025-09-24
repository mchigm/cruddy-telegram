#!/usr/bin/env python3
"""
Demo script showing YouTube Downloader functionality without GUI
This demonstrates the core downloading logic
"""

import sys
import time
from pathlib import Path
from pytube import YouTube
from config import get_downloads_directory, sanitize_filename

def demo_download(url):
    """Demo function showing how video download works"""
    print(f"Demo: Processing URL: {url}")
    
    try:
        # Create YouTube object
        print("Creating YouTube object...")
        yt = YouTube(url)
        
        print(f"Video Title: {yt.title}")
        print(f"Duration: {yt.length} seconds")
        print(f"Views: {yt.views}")
        print(f"Author: {yt.author}")
        
        # Get available streams
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        print(f"Available progressive MP4 streams: {len(streams)}")
        
        if streams:
            best_stream = streams.order_by('resolution').desc().first()
            print(f"Best quality: {best_stream.resolution}")
            print(f"File size: {best_stream.filesize} bytes ({best_stream.filesize / 1024 / 1024:.1f} MB)")
            
            # Prepare filename
            safe_title = sanitize_filename(yt.title)
            filename = f"{safe_title}.mp4"
            downloads_dir = get_downloads_directory()
            filepath = downloads_dir / filename
            
            print(f"Would save to: {filepath}")
            
            # In a real scenario, this would download:
            # best_stream.download(output_path=str(downloads_dir), filename=filename)
            print("✅ Demo completed successfully (no actual download in demo mode)")
            
        else:
            print("❌ No suitable progressive streams found")
            
            # Check adaptive streams
            adaptive_streams = yt.streams.filter(adaptive=True, file_extension='mp4')
            print(f"Available adaptive MP4 streams: {len(adaptive_streams)}")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def main():
    """Demo main function"""
    print("YouTube Downloader - Demo Mode")
    print("=" * 40)
    
    # Test configuration
    print("Testing configuration...")
    downloads_dir = get_downloads_directory()
    print(f"Downloads directory: {downloads_dir}")
    print(f"Directory exists: {downloads_dir.exists()}")
    
    # Test filename sanitization
    print("\nTesting filename sanitization...")
    test_titles = [
        "My Video: The Best!",
        "Video <with> invalid|chars",
        "Very Long Video Title That Exceeds The Maximum Length Limit And Should Be Truncated Properly",
        "Видео на русском языке",
        "Video/with\\slashes",
    ]
    
    for title in test_titles:
        safe = sanitize_filename(title)
        print(f"  '{title}' -> '{safe}'")
    
    # Demo video processing (without actual download due to network restrictions)
    print("\nDemo video processing...")
    demo_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    print("Note: Network access may be limited in this environment")
    
    try:
        demo_download(demo_url)
    except Exception as e:
        print(f"Network-related error (expected in restricted environment): {str(e)}")
    
    print("\n" + "=" * 40)
    print("Demo completed!")
    print("In a real environment with network access and wxPython installed,")
    print("run 'python youtube_downloader.py' to start the full GUI application.")

if __name__ == "__main__":
    main()