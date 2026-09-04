import re


def validate_player_id(player_id: str) -> bool:
    """Checks if the player id follows gaming platform standard."""
    pattern = r'^[a-zA-Z0-9_-]{3,16}$'
    return bool(re.match(pattern, player_id))


def validate_game_config(config: dict) -> bool:
    """Ensures required configuration keys are present."""
    required = {'server_region', 'max_players', 'tick_rate'}
    return required.issubset(config.keys())


def validate_coordinate_bounds(x: float, y: float, limit: float) -> bool:
    """Verifies world position stays within map boundaries."""
    return abs(x) <= limit and abs(y) <= limit


def sanitize_chat_input(message: str) -> str:
    """Removes potential injection characters from input strings."""
    # Simple stripping of control characters
    return re.sub(r'[\x00-\x1f\x7f]', '', message).strip()[:256]


def validate_session_token(token: str) -> bool:
    """Validates format of session authentication tokens."""
    return len(token) == 64 and token.isalnum()