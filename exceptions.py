class GameError(Exception):
    """Base class for game-related exceptions."""
    pass

class InvalidInputError(GameError):
    """Raised when the input is invalid."""
    def __init__(self, message):
        super().__init__(message)

class PlayerNotFoundError(GameError):
    """Raised when a player is not found in the game."""
    def __init__(self, player_id):
        super().__init__(f'Player with ID {player_id} not found.')

class LevelNotUnlockedError(GameError):
    """Raised when trying to access a level that is not unlocked."""
    def __init__(self, level_num):
        super().__init__(f'Level {level_num} is not unlocked.')

class InsufficientResourcesError(GameError):
    """Raised when there are not enough resources for an action."""
    def __init__(self, resource_name, required, available):
        super().__init__(f'Insufficient {resource_name}. Needed: {required}, Available: {available}.')

