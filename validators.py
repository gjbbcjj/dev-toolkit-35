import re


def is_valid_username(username: str) -> bool:
    """
    Validates the username for gaming accounts.
    Criteria:
    - Length: 3 to 16 characters
    - Characters: Alphanumeric and underscores only
    """
    pattern = r'^[a-zA-Z0-9_]{3,16}$'
    return bool(re.match(pattern, username))


def is_valid_email(email: str) -> bool:
    """
    Validates the email format for gaming accounts.
    Criteria:
    - Contains one '@' symbol
    - Valid domain name
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def is_valid_score(score: int) -> bool:
    """
    Validates if the score is within the acceptable range.
    Valid range is from 0 to 1000.
    """
    return 0 <= score <= 1000


def is_valid_game_id(game_id: str) -> bool:
    """
    Validates the game ID format.
    Criteria:
    - Must be 8 characters
    - Alphanumeric characters only
    """
    return len(game_id) == 8 and game_id.isalnum()