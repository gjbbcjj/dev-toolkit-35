from typing import Any

class CustomError(Exception):
    """
    Exception raised for custom application errors.
    """
    def __init__(self, message: str, code: int = 500) -> None:
        """
        Initialize CustomError with message and code.
        """
        super().__init__(message)
        self.message = message
        self.code = code

    def __str__(self) -> str:
        return f'CustomError({self.code}): {self.message}'

class NotFoundError(CustomError):
    """
    Exception raised when an item is not found.
    """
    def __init__(self, item: str) -> None:
        """
        Initialize NotFoundError for a specific item.
        """
        message = f'{item} not found.'
        super().__init__(message, code=404)

class ValidationError(CustomError):
    """
    Exception raised for validation errors.
    """
    def __init__(self, errors: Any) -> None:
        """
        Initialize ValidationError with a list of errors.
        """
        message = f'Validation errors: {errors}'
        super().__init__(message, code=400)
