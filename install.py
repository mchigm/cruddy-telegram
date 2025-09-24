#!/usr/bin/env python3
"""
Installation script for YouTube Downloader
Handles dependency installation and setup
"""

import sys
import subprocess
import platform
from pathlib import Path

def check_python_version():
    """Check Python version compatibility"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        print(f"   Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def install_dependencies():
    """Install required Python packages"""
    print("\nInstalling dependencies...")
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def check_system_requirements():
    """Check system-specific requirements"""
    system = platform.system().lower()
    print(f"\n🖥️  Detected system: {system}")
    
    if system == "linux":
        print("📋 For Linux users:")
        print("   If wxPython installation fails, install system packages:")
        print("   sudo apt-get install libgtk-3-dev libwebkitgtk-3.0-dev")
        print("   sudo apt-get install python3-dev build-essential")
        
    elif system == "darwin":  # macOS
        print("📋 For macOS users:")
        print("   Ensure Xcode command line tools are installed:")
        print("   xcode-select --install")
        
    elif system == "windows":
        print("📋 For Windows users:")
        print("   wxPython should install automatically with pip")
        
    return True

def create_desktop_shortcut():
    """Create desktop shortcuts where applicable"""
    system = platform.system().lower()
    
    if system == "windows":
        # Windows shortcut creation would require additional libraries
        print("💡 Windows: You can create a desktop shortcut manually to run.bat")
        
    elif system == "linux":
        desktop_dir = Path.home() / "Desktop"
        if desktop_dir.exists():
            shortcut_content = f"""[Desktop Entry]
Version=1.0
Type=Application
Name=YouTube Downloader
Comment=Download and play YouTube videos
Exec=python3 {Path.cwd() / 'youtube_downloader.py'}
Icon=applications-multimedia
Terminal=false
Categories=AudioVideo;Video;
"""
            shortcut_file = desktop_dir / "youtube-downloader.desktop"
            try:
                shortcut_file.write_text(shortcut_content)
                shortcut_file.chmod(0o755)
                print(f"✅ Desktop shortcut created: {shortcut_file}")
            except Exception as e:
                print(f"⚠️  Could not create desktop shortcut: {e}")
    
    elif system == "darwin":  # macOS
        print("💡 macOS: Use the build_executable.py script to create a .app bundle")

def main():
    """Main installation process"""
    print("YouTube Downloader - Installation")
    print("=" * 40)
    
    # Check current directory
    if not Path("youtube_downloader.py").exists():
        print("❌ Error: youtube_downloader.py not found")
        print("   Please run this script from the project directory")
        return 1
    
    # Check Python version
    if not check_python_version():
        return 1
    
    # Check system requirements
    check_system_requirements()
    
    # Install dependencies
    if not install_dependencies():
        return 1
    
    # Create shortcuts
    create_desktop_shortcut()
    
    print("\n" + "=" * 40)
    print("🎉 Installation completed successfully!")
    print("\nTo run the application:")
    print("  • Python: python youtube_downloader.py")
    print("  • Or use: python run.py")
    print("  • Windows: double-click run.bat")
    print("  • Linux/macOS: ./run.sh")
    print("\nTo create executable packages:")
    print("  • Run: python build_executable.py")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())