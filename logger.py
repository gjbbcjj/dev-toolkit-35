import logging


class Logger:
    """Class to handle logging for the application."""

    def __init__(self, name: str, level: int = logging.INFO) -> None:
        """Initialize the logger with a specific name and log level."""
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handler()

    def _setup_handler(self) -> None:
        """Set up console and file handlers for logging."""
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def debug(self, message: str) -> None:
        """Log a message with DEBUG level."""
        self.logger.debug(message)

    def info(self, message: str) -> None:
        """Log a message with INFO level."""
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """Log a message with WARNING level."""
        self.logger.warning(message)

    def error(self, message: str) -> None:
        """Log a message with ERROR level."""
        self.logger.error(message)

    def critical(self, message: str) -> None:
        """Log a message with CRITICAL level."""
        self.logger.critical(message)