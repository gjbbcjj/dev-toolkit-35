class GameError(Exception):
    """Base class for game-related exceptions."""
    pass

class InvalidInputError(GameError):
    """Exception raised for invalid input in the game."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

class GameNotFoundError(GameError):
    """Exception raised when a game is not found."""
    def __init__(self, game_id: int) -> None:
        super().__init__(f'Game not found: {game_id}')
        self.game_id = game_id

class PlayerError(GameError):
    """Base class for player-related exceptions."""
    pass

class PlayerNotFoundError(PlayerError):
    """Exception raised when a specified player is not found."""
    def __init__(self, player_id: int) -> None:
        super().__init__(f'Player not found: {player_id}')
        self.player_id = player_id

class MoveError(GameError):
    """Exception raised for errors during a player move."""
    pass

class InvalidMoveError(MoveError):
    """Exception raised for an invalid move made by a player."""
    def __init__(self, move: str) -> None:
        super().__init__(f'Invalid move: {move}')
        self.move = move
