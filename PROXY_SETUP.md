# Proxy Setup Guide for Geo-Restriction Bypass

This guide helps you configure proxy settings to download YouTube videos that may be restricted in your region.

## When Do You Need a Proxy?

You might need a proxy if you encounter these issues:
- Error messages about video not being available in your region
- "No suitable video stream found" for videos that should be downloadable
- Slow download speeds that suggest geo-throttling

## Setting up a Proxy

### Method 1: Edit config.py (Recommended)

1. Open the `config.py` file in your text editor
2. Find the proxy settings section (around line 27-34):

```python
# Proxy settings for geo-restriction bypass
ENABLE_PROXY = False  # Set to True to enable proxy support
PROXY_URL = None  # Format: "http://username:password@proxy.server:port" or "http://proxy.server:port"
```

3. Change the settings to enable your proxy:

```python
# Proxy settings for geo-restriction bypass
ENABLE_PROXY = True  # Enable proxy support
PROXY_URL = "http://your-proxy-server.com:8080"  # Replace with your proxy details
```

If your proxy requires authentication:
```python
PROXY_URL = "http://username:password@your-proxy-server.com:8080"
```

4. Save the file and restart the application

### Method 2: Environment Variables

Alternatively, you can set environment variables (this may work depending on your setup):

**Windows:**
```cmd
set http_proxy=http://your-proxy-server.com:8080
set https_proxy=http://your-proxy-server.com:8080
python youtube_downloader.py
```

**Linux/macOS:**
```bash
export http_proxy=http://your-proxy-server.com:8080
export https_proxy=http://your-proxy-server.com:8080
python youtube_downloader.py
```

## Finding a Proxy Server

### Free Proxy Services
- **ProxyList**: Various free proxy lists online (use with caution)
- **Public Proxies**: Often slow and unreliable, but free

### Paid Proxy Services (Recommended)
- **Private Proxy Providers**: More reliable and faster
- **VPN with HTTP Proxy**: Many VPN services offer HTTP proxy endpoints
- **Cloud Proxy Services**: Services like Bright Data, Oxylabs, etc.

### VPN Services with Proxy Support
Many VPN providers offer HTTP proxy endpoints that you can use instead of running their desktop app.

## Testing Your Proxy Configuration

1. After configuring your proxy, run the test script:
```bash
python test_core.py
```

2. Look for the "Testing geo-restriction bypass functionality" section in the output

3. If successful, you should see:
```
✅ Proxy configuration loaded: ['http', 'https']
✅ Enhanced session working correctly
```

## Troubleshooting

### Common Issues

**"Proxy configuration loaded" but downloads still fail:**
- Your proxy server might be blocked by YouTube
- Try a different proxy server from a different region
- Some proxies don't support HTTPS - try HTTP-only proxies

**"Enhanced session test failed":**
- Check your proxy URL format
- Verify the proxy server is working
- Test with a simple web browser first

**Authentication errors:**
- Make sure username and password are correct
- Some proxies use different authentication methods

### Testing Your Proxy Manually

You can test if your proxy works by using curl:
```bash
curl -x http://your-proxy-server.com:8080 https://httpbin.org/ip
```

This should return an IP address different from your real one.

## Security Considerations

- **Free proxies**: May log your traffic or inject ads
- **Paid proxies**: Generally more secure and reliable
- **Authentication**: Never use important passwords for proxy authentication
- **HTTPS**: The application uses HTTPS where possible to encrypt traffic

## Example Configurations

### Basic HTTP Proxy
```python
ENABLE_PROXY = True
PROXY_URL = "http://proxy.example.com:8080"
```

### Authenticated Proxy
```python
ENABLE_PROXY = True
PROXY_URL = "http://myusername:mypassword@proxy.example.com:8080"
```

### SOCKS Proxy (if supported by your setup)
```python
ENABLE_PROXY = True
PROXY_URL = "socks5://proxy.example.com:1080"
```

Note: SOCKS proxy support depends on your Python requests library configuration.

## Alternative Solutions

If proxy configuration doesn't work for you:

1. **Use a VPN**: Run a VPN client and use the application normally
2. **Change DNS**: Sometimes changing to public DNS (8.8.8.8, 1.1.1.1) helps
3. **Try different regions**: If using a proxy service, try servers from different countries
4. **Wait and retry**: Some restrictions are temporary

## Getting Help

If you're still having issues:
1. Check the main README.md troubleshooting section
2. Verify your proxy works with other applications first
3. Try the basic configuration examples above
4. Consider using a VPN as an alternative solution