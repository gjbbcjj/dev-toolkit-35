import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(log_file="game.log", max_bytes=1048576, backup_count=5):
    """
    Sets up a logger with console and rotating file handlers.
    
    Args:
        log_file (str): Path to the log file.
        max_bytes (int): Maximum size of log file before rotation (default 1MB).
        backup_count (int): Number of backup log files to keep.
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger("dev_toolkit")
    logger.setLevel(logging.DEBUG)
    
    # Avoid duplicate handlers if setup is called multiple times
    if logger.handlers:
        return logger

    # Create standard formatter for logs
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Console handler for terminal output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Rotating file handler to manage log size
    try:
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        file_handler = RotatingFileHandler(
            log_file, maxBytes=max_bytes, backupCount=backup_count
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except (OSError, PermissionError) as e:
        logger.warning(f"Failed to set up file logging: {e}")

    return logger