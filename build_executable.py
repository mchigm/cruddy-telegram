#!/usr/bin/env python3
"""
Build executable packages for YouTube Downloader
Supports creating .exe (Windows) and .app/.pkg (macOS) packages
"""

import os
import sys
import platform
import subprocess
from pathlib import Path

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    try:
        import PyInstaller
        print("PyInstaller is already installed")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

def build_executable():
    """Build executable for current platform"""
    install_pyinstaller()
    
    system = platform.system().lower()
    app_name = "YouTubeDownloader"
    
    # Common PyInstaller arguments
    args = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--windowed",
        "--name", app_name,
        "--add-data", "requirements.txt:.",
    ]
    
    # Platform-specific modifications
    if system == "windows":
        args.extend([
            "--icon", "icon.ico",  # Add icon if available
            "youtube_downloader.py"
        ])
        output_ext = ".exe"
    elif system == "darwin":  # macOS
        args.extend([
            "--icon", "icon.icns",  # Add icon if available
            "youtube_downloader.py"
        ])
        output_ext = ".app"
    else:  # Linux and others
        args.append("youtube_downloader.py")
        output_ext = ""
    
    print(f"Building executable for {system}...")
    print(f"Command: {' '.join(args)}")
    
    try:
        subprocess.check_call(args)
        
        # Find the created executable
        dist_dir = Path("dist")
        if system == "darwin":
            executable_path = dist_dir / f"{app_name}.app"
        else:
            executable_path = dist_dir / f"{app_name}{output_ext}"
        
        if executable_path.exists():
            print(f"✅ Executable created successfully: {executable_path}")
            
            # Create additional package formats
            if system == "darwin":
                create_dmg(app_name)
            elif system == "windows":
                create_installer(app_name)
                
        else:
            print("❌ Executable not found in expected location")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        return False
    
    return True

def create_dmg(app_name):
    """Create DMG package for macOS"""
    print("Creating DMG package...")
    try:
        # This is a simplified approach - in production, you'd use more sophisticated tools
        dmg_name = f"{app_name}.dmg"
        subprocess.check_call([
            "hdiutil", "create",
            "-volname", app_name,
            "-srcfolder", f"dist/{app_name}.app",
            "-ov", "-format", "UDZO",
            f"dist/{dmg_name}"
        ])
        print(f"✅ DMG created: dist/{dmg_name}")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("ℹ️  DMG creation skipped (hdiutil not available)")

def create_installer(app_name):
    """Create installer for Windows"""
    print("Windows installer creation would require NSIS or similar tools")
    print("For now, the .exe file in dist/ can be distributed directly")

def main():
    """Main entry point"""
    print("YouTube Downloader - Executable Builder")
    print("=" * 40)
    
    if not Path("youtube_downloader.py").exists():
        print("❌ youtube_downloader.py not found in current directory")
        return
    
    if not Path("requirements.txt").exists():
        print("❌ requirements.txt not found in current directory")
        return
    
    success = build_executable()
    
    if success:
        print("\n✅ Build completed successfully!")
        print("Check the 'dist' directory for your executable")
    else:
        print("\n❌ Build failed")

if __name__ == "__main__":
    main()