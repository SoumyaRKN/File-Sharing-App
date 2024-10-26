# File-Sharing-App
A simple Python application that allows you to share files from your local machine over the internet. It uses a local HTTP server and can be accessed through a public URL using Ngrok.

## Features

- Share files from any directory on your local machine.
- Simple command-line interface.
- Virtual environment management.
- Automatically installs dependencies.

## Requirements

- Python 3.x
- `pip` (Python package manager)
- Ngrok (for public URL sharing)

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

## Using Ngrok to Generate a Public Link

### 1. Download and Install Ngrok
Visit the [Ngrok website](https://ngrok.com/download) and download the appropriate version for your operating system.

### 2. Sign Up for a Free Account or Sign In to an Existing Account
- **To Sign Up**: Go to the [Ngrok signup page](https://dashboard.ngrok.com/signup) and create a free account. Once signed up, you will receive an authtoken in your dashboard.
  
- **To Sign In**: If you already have an account, go to the [Ngrok login page](https://dashboard.ngrok.com/login) and enter your credentials. After logging in, you will find your authtoken on the dashboard.


### 3. Authenticate Ngrok
In your terminal, run the following command, replacing `YOUR_AUTHTOKEN` with your actual Ngrok authtoken:
```bash
ngrok authtoken {YOUR_AUTHTOKEN}
```

### 4. Start Ngrok:
In your terminal, run the following command:
```bash
ngrok http 8080
```

### 5. Share the Link
Copy the provided public URL and share it with anyone you want to allow access to your shared files.  
They can open the URL in their browser to access the files you are serving.
