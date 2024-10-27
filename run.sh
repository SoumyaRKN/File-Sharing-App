#!/bin/bash

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[1;36m'
BLUE='\033[1;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print logo
logo() {
    echo -e "\n${CYAN}"
    echo -e "**************************************************************************************************"
    echo -e "******************************************  File Share  ******************************************"
    echo -e "**************************************************************************************************"
    echo -e "${NC}\n"
}

# Function to activate virtual environment
activate_venv() {
    # Check if the virtual environment is already activated
    if [[ "$VIRTUAL_ENV" != "" ]]; then
        echo -e "${GREEN}Virtual environment is already activated.${NC}"
    else
        echo -e "${CYAN}Activating virtual environment...${NC}"
        source .venv/bin/activate
        echo -e "${GREEN}Virtual environment activated.${NC}"
    fi
}

# Prompt for directory path
prompt_directory() {
    echo -e "${BLUE}Enter the full path of the directory to serve:${NC}"
    read directory
    if [[ -d "$directory" ]]; then
        echo -e "${GREEN}Directory exists. Starting the server...${NC}"
        python3 main.py "$directory"
    else
        echo -e "${RED}Error: The specified directory does not exist.${NC}"
        exit 1
    fi
}

# Show logo and activate virtual environment
logo
activate_venv

# Prompt for directory and run main script
prompt_directory
