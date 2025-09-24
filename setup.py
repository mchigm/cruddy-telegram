#!/usr/bin/env python3
"""
Setup script for YouTube Downloader
Creates executable packages for different platforms
"""

from setuptools import setup, find_packages
import sys
import os

# Read requirements
with open('requirements.txt', 'r') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

# Read README
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="youtube-downloader",
    version="1.0.0",
    description="A GUI application for downloading and playing YouTube videos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="MCHIGM",
    python_requires=">=3.8",
    py_modules=["youtube_downloader"],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'youtube-downloader=youtube_downloader:main',
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Multimedia :: Video",
        "Topic :: Internet :: WWW/HTTP",
    ],
    keywords="youtube downloader video gui wxpython",
)