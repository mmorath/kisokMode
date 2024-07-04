# -*- coding:utf-8 -*-

"""
Module: Logging Configuration
Description:
    This module configures logging for the entire application. It ensures that all modules
    use a consistent logging setup, which simplifies logging management and ensures 
    uniform log formatting across the application.

Author: Matthias Morath
Creation Date: 2024-07-02
Version: 1.0.0
License: MIT

Usage:
    Import this module in your main application entry point to configure logging for the
    entire application.

Example:
    import logging_config
"""

import logging
import sys

# Define log level and format
LOG_LEVEL = logging.INFO
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# Configure the root logger
logging.basicConfig(
    level=LOG_LEVEL,
    format=LOG_FORMAT,
    datefmt=DATE_FORMAT,
    handlers=[
        logging.StreamHandler(sys.stdout)  # Log to standard output
    ]
)

# Optional: Configure a file handler
# Uncomment the following lines to log to a file as well
# file_handler = logging.FileHandler('app.log')
# file_handler.setLevel(LOG_LEVEL)
# file_handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT))
# logging.getLogger().addHandler(file_handler)