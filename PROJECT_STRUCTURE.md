# YouTube Downloader - Project Structure

This document outlines the structure and components of the YouTube Downloader application.

## Core Files

### `youtube_downloader.py`
Main application file containing the wxPython GUI and core functionality:
- `YouTubeDownloaderFrame`: Main application window
- `VideoPlayerDialog`: Built-in video player
- `YouTubeDownloaderApp`: Application class
- Download management and progress tracking
- Video list management and playback

### `config.py`
Configuration settings and utility functions:
- Application constants and settings
- Directory management functions
- Filename sanitization utilities
- Cross-platform compatibility settings

### `requirements.txt`
Python package dependencies:
- `wxpython>=4.2.0`: GUI framework
- `pytube>=15.0.0`: YouTube video downloading
- `requests>=2.31.0`: HTTP requests
- `Pillow>=10.0.0`: Image processing support

## Launch Scripts

### `run.py`
Smart launcher with dependency checking:
- Python version validation
- Dependency availability checking
- Helpful error messages and installation guidance
- Automatic directory handling

### `run.bat` (Windows)
Windows batch file for easy launching:
- Double-click execution
- Error handling with pause

### `run.sh` (Linux/macOS)
Shell script for Unix-like systems:
- Executable permissions
- Python version detection
- Cross-platform compatibility

## Installation and Building

### `install.py`
Automated installation script:
- System requirements checking
- Dependency installation
- Desktop shortcut creation (Linux)
- Platform-specific guidance

### `setup.py`
Python packaging configuration:
- Package metadata
- Entry points definition
- Installation requirements
- Platform classifiers

### `build_executable.py`
Executable building script:
- PyInstaller integration
- Platform-specific packaging
- DMG creation (macOS)
- Installer preparation (Windows)

## Testing and Demo

### `test_core.py`
Core functionality tests:
- File operations testing
- Network connectivity checking
- Downloads directory management
- pytube functionality validation

### `demo.py`
Demonstration of core features:
- Configuration testing
- Filename sanitization demo
- Video processing workflow
- Network-independent testing

## Documentation

### `README.md`
Comprehensive user documentation:
- Feature overview
- Installation instructions
- Usage guide
- Troubleshooting tips
- Technical details

### `PROJECT_STRUCTURE.md` (this file)
Development documentation:
- Project architecture
- File descriptions
- Component relationships

### `LICENSE`
BSD 2-Clause License for the project

## Generated/Runtime Files

### `downloads/`
Directory for downloaded videos:
- Created automatically
- Excluded from version control
- User-configurable location

### `.gitignore`
Git ignore rules for:
- Python bytecode and cache files
- Virtual environments
- Downloaded videos
- Build artifacts
- IDE files
- OS-specific files

## Application Architecture

```
YouTube Downloader
├── GUI Layer (wxPython)
│   ├── Main Window (URL input, progress, video list)
│   └── Video Player (playback controls)
├── Core Logic
│   ├── YouTube Integration (pytube)
│   ├── File Management
│   └── Configuration Management
├── Platform Support
│   ├── Windows (.exe, .bat)
│   ├── macOS (.app, .dmg, .sh)
│   └── Linux (executable, .sh, .desktop)
└── Testing & Demo
    ├── Core Functionality Tests
    └── Demo Mode
```

## Key Features Implementation

1. **Cross-Platform GUI**: wxPython provides native look and feel
2. **Robust Downloads**: pytube handles YouTube API changes
3. **Progress Tracking**: Threading for non-blocking operations
4. **Video Management**: List, play, delete downloaded content
5. **Error Handling**: Comprehensive error messages and recovery
6. **Packaging Support**: Multiple distribution formats
7. **User-Friendly**: Simple installation and launch process

## Development Guidelines

- **Minimal Dependencies**: Only essential packages required
- **Cross-Platform**: Tested on Windows, macOS, and Linux
- **Error Resilient**: Graceful handling of network and file issues
- **User-Centric**: Clear interfaces and helpful messages
- **Maintainable**: Modular structure with clear separation of concerns