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

# Function to activate virtual environment
activate_venv() {
    # Check if the virtual environment is already activated
    if [[ "$VIRTUAL_ENV" != "" ]]; then
        echo -e "${GREEN}Virtual environment is already activated.${NC}"
    else
        echo -e "${LIGHT_BLUE}Activating virtual environment...${NC}"
        source .venv/bin/activate
        echo -e "${GREEN}Virtual environment activated.${NC}"
    fi
}

# Show logo and activate virtual environment
logo
activate_venv

# Run the bot main script
python3 main.py
