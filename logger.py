import logging

# Configure the logger settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class Logger:
    """ A simple logger class for the gaming toolkit. """

    @staticmethod
    def debug(message):
        logging.debug(message)

    @staticmethod
    def info(message):
        logging.info(message)

    @staticmethod
    def warning(message):
        logging.warning(message)

    @staticmethod
    def error(message):
        logging.error(message)

    @staticmethod
    def critical(message):
        logging.critical(message)

    @staticmethod
    def set_level(level):
        """ Set the logging level. """
        logging.getLogger().setLevel(level)  

# Example usage
if __name__ == '__main__':
    Logger.info('Logger initialized')
    Logger.debug('This is a debug message')
    Logger.error('This is an error message')