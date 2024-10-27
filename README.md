# File-Sharing-App
A simple Python application that allows you to share files.

## Overview
This application allows you to easily share files over a local network using a simple HTTP server. Users can access the shared files by opening a link in their web browser or scanning a QR code.

## Features

- Share files from any directory on your local machine.
- Simple command-line interface.
- Virtual environment management.
- Automatically installs dependencies.

## Requirements

- Python 3.x
- `pip` (Python package manager)

## Note:
- Both the sharing device and receiving device must be connected to the same network. This means they should either be on the same Wi-Fi network or connected to the hotspot of the sharing machine.

## Installation Instructions

### 1. Install The Application
You can install the application in one of two ways:

#### Option 1: Download The ZIP File
1. Go to the [GitHub repository](https://github.com/SoumyaRKN/File-Sharing-App).
2. Click on the green "Code" button and select "Download ZIP".
3. Extract the downloaded ZIP file to your desired location.

#### Option 2: Clone The Repository
If you have `git` installed, you can clone the repository using the following commands:
```bash
git clone https://github.com/SoumyaRKN/File-Sharing-App.git
cd File-Sharing-App
```

### 2. Setup And Run The Application
Setup and Run the application using following commands:
```bash
sudo bash setup.sh
sudo bash run.sh
```

## Supported File Types
The server supports downloading various file types, including but not limited to:

- Documents: .pdf, .doc, .docx, .xls, .xlsx, .ppt, .pptx, .txt
- Images: .png, .jpg, .jpeg, .gif, .bmp, .tiff, .svg
- Audio: .mp3, .wav, .aac, .ogg, .flac
- Video: .mp4, .avi, .mkv, .mov
- Archives: .zip, .rar, .tar, .gz, .7z
- Code Files: .js, .py, .html, .css
- Other: .epub, .mobi
