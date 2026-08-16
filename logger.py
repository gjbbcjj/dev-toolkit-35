import logging
from logging.handlers import RotatingFileHandler

# Logger configuration function

def setup_logger(log_file='game.log', max_bytes=5*1024*1024, backup_count=3):
    """
    Set up a logger that rotates log files when they reach a certain size.
    :param log_file: File name for the log file
    :param max_bytes: Maximum file size in bytes before rotation
    :param backup_count: Number of backup files to keep
    """
    logger = logging.getLogger('GameLogger')
    logger.setLevel(logging.DEBUG)

    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger

if __name__ == '__main__':
    logger = setup_logger()
    logger.debug('Logger is set up and ready to go!')