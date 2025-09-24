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

# Proxy settings for geo-restriction bypass
ENABLE_PROXY = False  # Set to True to enable proxy support
PROXY_URL = None  # Format: "http://username:password@proxy.server:port" or "http://proxy.server:port"
PROXY_DICT = None  # Will be auto-generated from PROXY_URL if provided

# Region bypass settings
USE_OAUTH = False  # Disable OAuth to avoid region checks
USE_PO_TOKEN = False  # Disable po_token to avoid additional restrictions
BYPASS_AGE_GATE = True  # Try to bypass age-restricted content

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

def configure_proxy():
    """Configure proxy settings from PROXY_URL"""
    global PROXY_DICT
    if ENABLE_PROXY and PROXY_URL:
        PROXY_DICT = {
            'http': PROXY_URL,
            'https': PROXY_URL
        }
    else:
        PROXY_DICT = None
    return PROXY_DICT

def get_proxy_config():
    """Get the current proxy configuration"""
    if not PROXY_DICT and ENABLE_PROXY:
        configure_proxy()
    return PROXY_DICT

def get_custom_headers():
    """Get custom headers for requests"""
    return {
        'User-Agent': USER_AGENT,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-us,en;q=0.5',
        'Accept-Encoding': 'gzip,deflate',
        'Connection': 'keep-alive'
    }

# Export commonly used functions and constants
__all__ = [
    'APP_NAME', 'APP_VERSION', 'APP_AUTHOR',
    'DEFAULT_WINDOW_SIZE', 'DEFAULT_PLAYER_SIZE',
    'get_downloads_directory', 'get_config_directory',
    'sanitize_filename', 'REQUEST_TIMEOUT',
    'get_proxy_config', 'get_custom_headers', 'configure_proxy',
    'USE_OAUTH', 'USE_PO_TOKEN', 'BYPASS_AGE_GATE'
]