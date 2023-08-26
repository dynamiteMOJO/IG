
# Provides logging functionalities

import logging

# Set up logging
logging.basicConfig(filename='./logs/bot_log.txt', level=logging.INFO)

def log_message(message):
    """Log a specific message to the log file."""
    logging.info(message)
