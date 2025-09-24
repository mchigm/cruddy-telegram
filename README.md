# YouTube Downloader

A cross-platform GUI application for downloading and playing YouTube videos locally. This application works even in regions where YouTube access may be restricted.

## Features

- **Easy-to-use GUI**: Built with wxPython for a native look and feel
- **YouTube Video Download**: Download videos in MP4 format with the best available quality
- **Built-in Video Player**: Play downloaded videos directly within the application
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Region-friendly**: Download videos even from restricted locations with enhanced geo-bypass
- **Proxy Support**: Configure HTTP/HTTPS proxies for additional privacy and geo-restriction bypass
- **Custom Headers**: Uses optimized headers to improve download success rates
- **Batch Management**: View, play, and delete downloaded videos

## Requirements

- Python 3.8 or higher
- wxPython 4.2.0+
- pytube 15.0.0+
- requests 2.31.0+

## Installation

### From Source

1. Clone the repository:
```bash
git clone https://github.com/mchigm/cruddy-telegram.git
cd cruddy-telegram
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python youtube_downloader.py
```

### Executable Packages

You can create standalone executable packages:

```bash
python build_executable.py
```

This will create platform-specific executables in the `dist/` directory:
- Windows: `.exe` file
- macOS: `.app` bundle and `.dmg` package
- Linux: executable binary

## Quick Proxy Setup

If videos are blocked in your region, you can quickly enable proxy support:

1. **Edit config.py** and change:
```python
ENABLE_PROXY = True
PROXY_URL = "http://your-proxy-server:port"
```

2. **Test your configuration**:
```bash
python test_proxy.py
```

3. **Run the application**:
```bash
python youtube_downloader.py
```

For detailed proxy setup instructions, see [PROXY_SETUP.md](PROXY_SETUP.md).

## Usage

1. **Launch the application**: Run `python youtube_downloader.py` or use the executable
2. **Enter YouTube URL**: Paste any valid YouTube video URL in the input field
3. **Download**: Click the "Download" button to start downloading
4. **Monitor Progress**: Watch the progress bar and status messages
5. **Play Videos**: Select a downloaded video from the list and click "Play Selected"
6. **Manage Videos**: Use "Refresh List" to update the list or "Delete Selected" to remove videos

## Configuration

### Proxy Support for Geo-Restriction Bypass

If you're experiencing issues downloading videos due to geo-restrictions, you can configure a proxy:

1. **Edit config.py** and modify the proxy settings:
```python
# Enable proxy support
ENABLE_PROXY = True
PROXY_URL = "http://your-proxy-server:port"
# For authenticated proxies:
# PROXY_URL = "http://username:password@proxy-server:port"
```

2. **Alternative: Set environment variables** (if supported):
```bash
export http_proxy=http://your-proxy-server:port
export https_proxy=http://your-proxy-server:port
```

### Region Bypass Settings

The application includes several built-in region bypass features:
- **Custom Headers**: Uses browser-like headers to improve access
- **Session Management**: Optimized request sessions for better compatibility
- **Multiple Stream Fallbacks**: Tries different stream types when geo-restricted

These settings are automatically applied and help bypass many common geo-restrictions without requiring a VPN.

## Screenshots

The application features:
- Clean, intuitive interface
- Real-time download progress
- List of downloaded videos with size information
- Built-in video player with basic controls

## Technical Details

- **Download Engine**: Uses `pytube` library for robust YouTube video extraction
- **GUI Framework**: wxPython for cross-platform native UI
- **Video Player**: Built-in wxPython MediaCtrl for video playback
- **Threading**: Non-blocking downloads with progress callbacks
- **File Management**: Automatic organization of downloaded videos

## Troubleshooting

### Common Issues

1. **"No suitable video stream found"**: Some videos may not be available for download due to restrictions
   - **Solution**: Try enabling proxy support in config.py or use a VPN
2. **Download fails with geo-restriction errors**: Video blocked in your region
   - **Solution**: Configure a proxy server in config.py (see Configuration section above)
   - **Alternative**: Use a VPN service to change your apparent location
3. **Download fails**: Check your internet connection and ensure the YouTube URL is valid
4. **Video won't play**: Ensure you have proper video codecs installed on your system
5. **Slow downloads**: This may indicate geo-throttling
   - **Solution**: Try using a proxy server from a different region

### Dependencies Issues

If you encounter issues with wxPython installation:

- **Linux**: Install system packages: `sudo apt-get install libgtk-3-dev libwebkitgtk-3.0-dev`
- **macOS**: Ensure Xcode command line tools are installed: `xcode-select --install`
- **Windows**: Usually works out of the box with pip

## License

This project is licensed under the BSD 2-Clause License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Disclaimer

This tool is for educational and personal use only. Please respect YouTube's Terms of Service and copyright laws. The developers are not responsible for any misuse of this software.
