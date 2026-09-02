class GameError(Exception):
    """Base exception for game errors."""
    pass

class InvalidMoveError(GameError):
    """Raised for invalid moves in the game."""
    pass

class GameCore:
    """Core logic for a simple tic-tac-toe game with robust error handling."""
    def __init__(self):
        self.board = [None] * 9
        self.current_player = 'X'
        self.game_over = False

    def make_move(self, position, player):
        """Make a move with checks for all edge cases."""
        if self.game_over:
            raise InvalidMoveError("Cannot move: game is over")
        if not isinstance(position, int):
            raise InvalidMoveError("Position must be an integer")
        if position < 0 or position > 8:
            raise InvalidMoveError("Position out of bounds: must be 0-8")
        if self.board[position] is not None:
            raise InvalidMoveError("Position already taken")
        if player != self.current_player:
            raise InvalidMoveError("Wrong player: not your turn")
        self.board[position] = player
        if self._check_winner(player):
            self.game_over = True
            return f"Player {player} wins!"
        if all(cell is not None for cell in self.board):
            self.game_over = True
            return "Game ended in a draw"
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return "Move successful"

    def _check_winner(self, player):
        """Check for winning combinations."""
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] == player:
                return True
        return False

    def get_board(self):
        """Return current board state."""
        return self.board.copy()

    def reset_game(self):
        """Reset the game to initial state."""
        self.board = [None] * 9
        self.current_player = 'X'
        self.game_over = False

# Demonstration of error handling
if __name__ == "__main__":
    game = GameCore()
    moves = [(0, 'X'), (1, 'O'), (0, 'X'), (3, 'O'), (4, 'X'), (5, 'O'), (8, 'X')]
    for pos, pl in moves:
        try:
            result = game.make_move(pos, pl)
            print(result)
        except InvalidMoveError as e:
            print(f"Handled error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
