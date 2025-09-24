#!/usr/bin/env python3
"""
YouTube Downloader Application
A GUI application for downloading and playing YouTube videos
"""

import os
import sys
import time
import threading
from pathlib import Path

import wx
import wx.media
from pytube import YouTube
import requests


class YouTubeDownloaderFrame(wx.Frame):
    """Main application frame for YouTube downloader"""
    
    def __init__(self):
        super().__init__(None, title="YouTube Downloader", size=(800, 600))
        
        # Create downloads directory
        self.downloads_dir = Path("downloads")
        self.downloads_dir.mkdir(exist_ok=True)
        
        # Initialize UI
        self.init_ui()
        
        # Center the window
        self.Center()
        
    def init_ui(self):
        """Initialize the user interface"""
        panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Title
        title = wx.StaticText(panel, label="YouTube Video Downloader")
        title_font = title.GetFont()
        title_font.PointSize += 4
        title_font = title_font.Bold()
        title.SetFont(title_font)
        main_sizer.Add(title, 0, wx.ALL | wx.CENTER, 10)
        
        # URL input section
        url_sizer = wx.BoxSizer(wx.HORIZONTAL)
        url_label = wx.StaticText(panel, label="YouTube URL:")
        self.url_text = wx.TextCtrl(panel, size=(400, -1))
        self.download_btn = wx.Button(panel, label="Download")
        
        url_sizer.Add(url_label, 0, wx.ALL | wx.CENTER, 5)
        url_sizer.Add(self.url_text, 1, wx.ALL | wx.EXPAND, 5)
        url_sizer.Add(self.download_btn, 0, wx.ALL, 5)
        
        main_sizer.Add(url_sizer, 0, wx.ALL | wx.EXPAND, 10)
        
        # Progress bar
        self.progress = wx.Gauge(panel, range=100)
        main_sizer.Add(self.progress, 0, wx.ALL | wx.EXPAND, 10)
        
        # Status text
        self.status_text = wx.StaticText(panel, label="Ready to download")
        main_sizer.Add(self.status_text, 0, wx.ALL | wx.CENTER, 5)
        
        # Video list
        list_label = wx.StaticText(panel, label="Downloaded Videos:")
        main_sizer.Add(list_label, 0, wx.ALL, 5)
        
        self.video_list = wx.ListCtrl(panel, style=wx.LC_REPORT | wx.LC_SINGLE_SEL)
        self.video_list.AppendColumn("Title", width=400)
        self.video_list.AppendColumn("Duration", width=100)
        self.video_list.AppendColumn("Size", width=100)
        self.video_list.AppendColumn("File", width=200)
        
        main_sizer.Add(self.video_list, 1, wx.ALL | wx.EXPAND, 10)
        
        # Control buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.play_btn = wx.Button(panel, label="Play Selected")
        self.refresh_btn = wx.Button(panel, label="Refresh List")
        self.delete_btn = wx.Button(panel, label="Delete Selected")
        
        self.play_btn.Enable(False)
        self.delete_btn.Enable(False)
        
        button_sizer.Add(self.play_btn, 0, wx.ALL, 5)
        button_sizer.Add(self.refresh_btn, 0, wx.ALL, 5)
        button_sizer.Add(self.delete_btn, 0, wx.ALL, 5)
        
        main_sizer.Add(button_sizer, 0, wx.ALL | wx.CENTER, 5)
        
        panel.SetSizer(main_sizer)
        
        # Bind events
        self.download_btn.Bind(wx.EVT_BUTTON, self.on_download)
        self.play_btn.Bind(wx.EVT_BUTTON, self.on_play)
        self.refresh_btn.Bind(wx.EVT_BUTTON, self.on_refresh)
        self.delete_btn.Bind(wx.EVT_BUTTON, self.on_delete)
        self.video_list.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_video_selected)
        self.video_list.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.on_video_deselected)
        
        # Load existing videos
        self.refresh_video_list()
        
    def on_download(self, event):
        """Handle download button click"""
        url = self.url_text.GetValue().strip()
        if not url:
            wx.MessageBox("Please enter a YouTube URL", "Error", wx.OK | wx.ICON_ERROR)
            return
            
        # Disable download button during download
        self.download_btn.Enable(False)
        self.progress.SetValue(0)
        self.status_text.SetLabel("Starting download...")
        
        # Start download in separate thread
        thread = threading.Thread(target=self.download_video, args=(url,))
        thread.daemon = True
        thread.start()
        
    def download_video(self, url):
        """Download video from YouTube URL"""
        try:
            # Update status
            wx.CallAfter(self.status_text.SetLabel, "Fetching video information...")
            
            # Create YouTube object
            yt = YouTube(url, on_progress_callback=self.progress_callback)
            
            # Get the highest quality progressive stream
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            
            if not stream:
                # Fallback to adaptive stream
                stream = yt.streams.filter(adaptive=True, file_extension='mp4').order_by('resolution').desc().first()
            
            if not stream:
                wx.CallAfter(wx.MessageBox, "No suitable video stream found", "Error", wx.OK | wx.ICON_ERROR)
                return
                
            # Clean filename
            safe_title = "".join(c for c in yt.title if c.isalnum() or c in (' ', '-', '_')).rstrip()
            filename = f"{safe_title}.mp4"
            filepath = self.downloads_dir / filename
            
            # Update status
            wx.CallAfter(self.status_text.SetLabel, f"Downloading: {yt.title}")
            
            # Download the video
            stream.download(output_path=str(self.downloads_dir), filename=filename)
            
            # Update UI
            wx.CallAfter(self.status_text.SetLabel, f"Download completed: {yt.title}")
            wx.CallAfter(self.progress.SetValue, 100)
            wx.CallAfter(self.refresh_video_list)
            wx.CallAfter(self.url_text.SetValue, "")
            
        except Exception as e:
            error_msg = f"Download failed: {str(e)}"
            wx.CallAfter(wx.MessageBox, error_msg, "Error", wx.OK | wx.ICON_ERROR)
            wx.CallAfter(self.status_text.SetLabel, "Download failed")
        finally:
            wx.CallAfter(self.download_btn.Enable, True)
            
    def progress_callback(self, stream, chunk, bytes_remaining):
        """Callback for download progress"""
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = int((bytes_downloaded / total_size) * 100)
        wx.CallAfter(self.progress.SetValue, percentage)
        
    def refresh_video_list(self):
        """Refresh the list of downloaded videos"""
        self.video_list.DeleteAllItems()
        
        if not self.downloads_dir.exists():
            return
            
        video_files = list(self.downloads_dir.glob("*.mp4"))
        
        for i, video_file in enumerate(video_files):
            # Get file size
            size_mb = video_file.stat().st_size / (1024 * 1024)
            size_str = f"{size_mb:.1f} MB"
            
            # Add to list (we don't have duration info for now)
            index = self.video_list.InsertItem(i, video_file.stem)
            self.video_list.SetItem(index, 1, "Unknown")  # Duration
            self.video_list.SetItem(index, 2, size_str)   # Size
            self.video_list.SetItem(index, 3, video_file.name)  # Filename
            
    def on_refresh(self, event):
        """Handle refresh button click"""
        self.refresh_video_list()
        
    def on_video_selected(self, event):
        """Handle video selection"""
        self.play_btn.Enable(True)
        self.delete_btn.Enable(True)
        
    def on_video_deselected(self, event):
        """Handle video deselection"""
        self.play_btn.Enable(False)
        self.delete_btn.Enable(False)
        
    def on_play(self, event):
        """Handle play button click"""
        selected = self.video_list.GetFirstSelected()
        if selected == -1:
            return
            
        filename = self.video_list.GetItemText(selected, 3)
        filepath = self.downloads_dir / filename
        
        if not filepath.exists():
            wx.MessageBox("Video file not found", "Error", wx.OK | wx.ICON_ERROR)
            return
            
        # Open video player dialog
        player_dialog = VideoPlayerDialog(self, str(filepath))
        player_dialog.ShowModal()
        player_dialog.Destroy()
        
    def on_delete(self, event):
        """Handle delete button click"""
        selected = self.video_list.GetFirstSelected()
        if selected == -1:
            return
            
        filename = self.video_list.GetItemText(selected, 3)
        filepath = self.downloads_dir / filename
        
        # Confirm deletion
        dlg = wx.MessageDialog(self, f"Are you sure you want to delete '{filename}'?", 
                              "Confirm Delete", wx.YES_NO | wx.ICON_QUESTION)
        
        if dlg.ShowModal() == wx.ID_YES:
            try:
                filepath.unlink()
                self.refresh_video_list()
                self.status_text.SetLabel(f"Deleted: {filename}")
            except Exception as e:
                wx.MessageBox(f"Failed to delete file: {str(e)}", "Error", wx.OK | wx.ICON_ERROR)
        
        dlg.Destroy()


class VideoPlayerDialog(wx.Dialog):
    """Simple video player dialog"""
    
    def __init__(self, parent, video_path):
        super().__init__(parent, title="Video Player", size=(640, 480))
        
        self.video_path = video_path
        self.init_ui()
        self.Center()
        
    def init_ui(self):
        """Initialize the video player UI"""
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Video display area
        self.media_ctrl = wx.media.MediaCtrl(panel, style=wx.SIMPLE_BORDER)
        sizer.Add(self.media_ctrl, 1, wx.ALL | wx.EXPAND, 5)
        
        # Control buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.play_btn = wx.Button(panel, label="Play")
        self.pause_btn = wx.Button(panel, label="Pause")
        self.stop_btn = wx.Button(panel, label="Stop")
        self.close_btn = wx.Button(panel, label="Close")
        
        button_sizer.Add(self.play_btn, 0, wx.ALL, 5)
        button_sizer.Add(self.pause_btn, 0, wx.ALL, 5)
        button_sizer.Add(self.stop_btn, 0, wx.ALL, 5)
        button_sizer.AddStretchSpacer()
        button_sizer.Add(self.close_btn, 0, wx.ALL, 5)
        
        sizer.Add(button_sizer, 0, wx.ALL | wx.EXPAND, 5)
        
        panel.SetSizer(sizer)
        
        # Bind events
        self.play_btn.Bind(wx.EVT_BUTTON, self.on_play)
        self.pause_btn.Bind(wx.EVT_BUTTON, self.on_pause)
        self.stop_btn.Bind(wx.EVT_BUTTON, self.on_stop)
        self.close_btn.Bind(wx.EVT_BUTTON, self.on_close)
        
        # Load video
        self.load_video()
        
    def load_video(self):
        """Load the video file"""
        try:
            if not self.media_ctrl.Load(self.video_path):
                wx.MessageBox("Failed to load video file", "Error", wx.OK | wx.ICON_ERROR)
        except Exception as e:
            wx.MessageBox(f"Error loading video: {str(e)}", "Error", wx.OK | wx.ICON_ERROR)
            
    def on_play(self, event):
        """Play the video"""
        self.media_ctrl.Play()
        
    def on_pause(self, event):
        """Pause the video"""
        self.media_ctrl.Pause()
        
    def on_stop(self, event):
        """Stop the video"""
        self.media_ctrl.Stop()
        
    def on_close(self, event):
        """Close the dialog"""
        self.media_ctrl.Stop()
        self.EndModal(wx.ID_OK)


class YouTubeDownloaderApp(wx.App):
    """Main application class"""
    
    def OnInit(self):
        frame = YouTubeDownloaderFrame()
        frame.Show()
        return True


def main():
    """Main entry point"""
    app = YouTubeDownloaderApp()
    app.MainLoop()


if __name__ == "__main__":
    main()