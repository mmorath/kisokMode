#!/bin/bash

# Clear the terminal screen
clear

# Start timing
start_time=$SECONDS

# Script Header
echo "############################################################################"
echo "##### Script for preparing the environment                             #####"
echo "##### author: Ihr Matthias Morath 2024-07-04                           #####"
echo "##### tested on:                                                       #####"
echo "#####  -Ubuntu 20.04.01                                                #####"
echo "############################################################################"

# Global settings
OE_CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Function to get the current OS user
get_current_user() {
    echo $USER
}

# Getting the current OS and User
OE_CURRENT_USER=$(get_current_user)
echo "############################################################################"
echo "### OS: $(uname)"
echo "### Current Directory: $OE_CURRENT_DIR"
echo "### Current User: $OE_CURRENT_USER"
echo "############################################################################"

# Check for virtual environment and create if it doesn't exist
echo "############################################################################"
echo "#### Checking if virtual environment exists"
echo "############################################################################"
if [ ! -d "$OE_CURRENT_DIR/venv" ]; then
    echo "#### Virtual environment does not exist, creating now..."
    python3 -m venv "$OE_CURRENT_DIR/venv"
else
    echo "#### Virtual environment already exists."
fi

# Activate the virtual environment
echo "#### Activating the virtual environment..."
source "$OE_CURRENT_DIR/venv/bin/activate"

# Display which python and pip are being used post-activation
echo "#### Using Python and pip from virtual environment"
which python
python --version
which pip
pip --version

# Install the requirements
if [ -f "$OE_CURRENT_DIR/requirements.txt" ]; then
    echo "#### Installing requirements from requirements.txt..."
    pip install wheel
    pip install -r "$OE_CURRENT_DIR/requirements.txt"
else
    echo "#### No requirements.txt found, skipping installation of packages."
fi

echo "#### Environment setup complete!"

# End timing and calculate duration
end_time=$SECONDS
duration=$(( end_time - start_time ))

echo "############################################################################"
echo "Script execution time: $duration seconds."
echo "############################################################################"
