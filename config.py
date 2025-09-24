#!/usr/bin/env python3
"""
Configuration settings for YouTube Downloader
"""

import os
from pathlib import Path

# Application settings
APP_NAME = "YouTube Downloader"
APP_VERSION = "1.0.0"
APP_AUTHOR = "MCHIGM"

# Default directories
DEFAULT_DOWNLOADS_DIR = Path("downloads")
DEFAULT_CONFIG_DIR = Path.home() / ".youtube-downloader"

# GUI settings
DEFAULT_WINDOW_SIZE = (800, 600)
DEFAULT_PLAYER_SIZE = (640, 480)

# Download settings
DEFAULT_VIDEO_FORMAT = "mp4"
DEFAULT_AUDIO_FORMAT = "mp3"
PREFERRED_QUALITY = "highest"  # Options: "highest", "lowest", "720p", "480p", etc.

# Network settings
REQUEST_TIMEOUT = 30  # seconds
MAX_RETRIES = 3
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# File naming settings
MAX_FILENAME_LENGTH = 100
INVALID_CHARS = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
REPLACEMENT_CHAR = '_'

# Video player settings
ENABLE_FULLSCREEN = True
ENABLE_CONTROLS = True
AUTO_PLAY = False

def get_downloads_directory():
    """Get the downloads directory, creating it if necessary"""
    downloads_dir = DEFAULT_DOWNLOADS_DIR
    downloads_dir.mkdir(exist_ok=True)
    return downloads_dir

def get_config_directory():
    """Get the config directory, creating it if necessary"""
    config_dir = DEFAULT_CONFIG_DIR
    config_dir.mkdir(exist_ok=True)
    return config_dir

def sanitize_filename(filename):
    """Sanitize filename by removing invalid characters"""
    # Remove invalid characters
    for char in INVALID_CHARS:
        filename = filename.replace(char, REPLACEMENT_CHAR)
    
    # Limit length
    if len(filename) > MAX_FILENAME_LENGTH:
        # Keep extension if present
        if '.' in filename:
            name, ext = filename.rsplit('.', 1)
            max_name_length = MAX_FILENAME_LENGTH - len(ext) - 1
            filename = name[:max_name_length] + '.' + ext
        else:
            filename = filename[:MAX_FILENAME_LENGTH]
    
    # Remove leading/trailing spaces and dots
    filename = filename.strip(' .')
    
    # Ensure filename is not empty
    if not filename:
        filename = "video"
    
    return filename

# Export commonly used functions and constants
__all__ = [
    'APP_NAME', 'APP_VERSION', 'APP_AUTHOR',
    'DEFAULT_WINDOW_SIZE', 'DEFAULT_PLAYER_SIZE',
    'get_downloads_directory', 'get_config_directory',
    'sanitize_filename', 'REQUEST_TIMEOUT'
]