# YouTube Downloader

A cross-platform GUI application for downloading and playing YouTube videos locally. This application works even in regions where YouTube access may be restricted.

## Features

- **Easy-to-use GUI**: Built with wxPython for a native look and feel
- **YouTube Video Download**: Download videos in MP4 format with the best available quality
- **Built-in Video Player**: Play downloaded videos directly within the application
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Region-friendly**: Download videos even from restricted locations
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

## Usage

1. **Launch the application**: Run `python youtube_downloader.py` or use the executable
2. **Enter YouTube URL**: Paste any valid YouTube video URL in the input field
3. **Download**: Click the "Download" button to start downloading
4. **Monitor Progress**: Watch the progress bar and status messages
5. **Play Videos**: Select a downloaded video from the list and click "Play Selected"
6. **Manage Videos**: Use "Refresh List" to update the list or "Delete Selected" to remove videos

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
2. **Download fails**: Check your internet connection and ensure the YouTube URL is valid
3. **Video won't play**: Ensure you have proper video codecs installed on your system

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
