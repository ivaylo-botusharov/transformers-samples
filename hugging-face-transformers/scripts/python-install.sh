#!/bin/bash

# Download the latest Python 3 installer for macOS
curl -O https://www.python.org/ftp/python/3.10.11/python-3.10.11-macos11.pkg

# Install Python 3 in silent mode
sudo installer -pkg python-3.10.11-macos11.pkg -target /

# Delete the downloaded Python .pkg file
rm python-3.10.11-macos11.pkg

sudo -H pip3 install --upgrade pip

sudo -H /Applications/Python\ 3.10/Install\ Certificates.command
