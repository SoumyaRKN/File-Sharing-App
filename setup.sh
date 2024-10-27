#!/bin/bash

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
LIGHT_BLUE='\033[1;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print logo
logo() {
    echo -e "\n${LIGHT_BLUE}"
    echo -e "**************************************************************************************************"
    echo -e "******************************************  File Share  ******************************************"
    echo -e "**************************************************************************************************"
    echo -e "${NC}\n"
}

# Function to show usage information
show_usage() {
    echo -e "\n${LIGHT_BLUE}"
    echo -e "Setup Completed. To Start The File Sharing Server:"
    echo -e "   1. Execute 'run.sh'"
    echo -e "   2. Enter the full directory path to serve when prompted."
    echo -e "Press Ctrl+C to stop the server."
    echo -e "${NC}\n"
    exit 1
}

# Function to detect the operating system
detect_os() {
    OS="$(uname -s)"
    
    case "$OS" in
        Linux*)     machine="LINUX";;
        Darwin*)    machine="MAC";;
        *)          echo -e "${RED}Unsupported OS: ${OS}${NC}"; exit 1;;
    esac

    echo -e "${LIGHT_BLUE}Detected OS: $machine${NC}"
}

# Function to check if a command exists
check_command() {
    command -v "$1" &> /dev/null
}

# Function to check and install Python if not installed
check_python() {
    if ! check_command "python3"; then
        echo -e "${YELLOW}Python is not installed. Attempting to install...${NC}"

        if [[ "$machine" == "LINUX" ]]; then
            if check_command "apt"; then
                sudo apt update && sudo apt install -y python3
            else
                echo -e "${RED}Package manager apt not found. Install Python manually.${NC}"
                exit 1
            fi
        elif [[ "$machine" == "MAC" ]]; then
            if check_command "brew"; then
                brew install python
            else
                echo -e "${RED}Homebrew not found. Install Python manually.${NC}"
                exit 1
            fi
        else
            echo -e "${RED}Automatic installation not supported on this OS. Please install Python 3 manually and rerun the script.${NC}"
            exit 1
        fi
    else
        echo -e "${LIGHT_BLUE}Python already installed.${NC}"
    fi
}

# Function to create or activate a virtual environment
venv_setup() {
    # Check if the virtual environment already exists
    if [[ -d ".venv" ]]; then
        echo -e "${LIGHT_BLUE}Virtual environment already exists.${NC}"
    else
        # Create the virtual environment if it does not exist
        echo -e "${LIGHT_BLUE}Creating virtual environment...${NC}"
        python3 -m venv .venv
        echo -e "${GREEN}Virtual environment created.${NC}"
    fi

    # Check if the virtual environment is already activated
    if [[ "$VIRTUAL_ENV" != "" ]]; then
        echo -e "${GREEN}Virtual environment is already activated.${NC}"
    else
        echo -e "${LIGHT_BLUE}Activating virtual environment...${NC}"
        source .venv/bin/activate
        echo -e "${GREEN}Virtual environment activated.${NC}"
    fi
}

# Function to install dependencies from 'requirements.txt' or manually if not found
install_packages() {
    local PIP="python3 -m pip"

    # Default packages to install if requirements.txt is not found
    local DEFAULT_PACKAGES=("qrcode" "pillow")

    if [[ ! -f "./requirements.txt" ]]; then
        echo -e "${YELLOW}requirements.txt not found. Checking for default packages to install...${NC}"

        # Loop through each default package and check if it's installed
        for package in "${DEFAULT_PACKAGES[@]}"; do
            if ! $PIP show "$package" &> /dev/null; then
                echo -e "${LIGHT_BLUE}Installing ${package}...${NC}"
                $PIP install "$package"
            else
                echo -e "${GREEN}${package} is already installed.${NC}"
            fi
        done
    else
        echo -e "${LIGHT_BLUE}Installing dependencies from requirements.txt...${NC}"

        # Read the requirements.txt and check for each package
        while IFS= read -r package; do
            # Ignore comments and empty lines
            if [[ -z "$package" || "$package" == \#* ]]; then
                continue
            fi

            if ! $PIP show "$package" &> /dev/null; then
                echo -e "${LIGHT_BLUE}Installing ${package}...${NC}"
                $PIP install "$package"
            else
                echo -e "${GREEN}${package} is already installed.${NC}"
            fi
        done < ./requirements.txt
    fi

    echo -e "${GREEN}Package installation completed.${NC}"
}


# Main Script
logo
detect_os
check_python
venv_setup
install_packages
show_usage
