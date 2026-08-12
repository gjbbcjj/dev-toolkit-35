import json
from typing import Any, Dict, List

class GameProcessor:
    def __init__(self, game_data: List[Dict[str, Any]]) -> None:
        self.game_data = game_data

    def process(self) -> List[Dict[str, Any]]:
        processed_data = []
        for game in self.game_data:
            processed_game = self._process_game(game)
            processed_data.append(processed_game)
        return processed_data

    def _process_game(self, game: Dict[str, Any]) -> Dict[str, Any]:
        # Transform the game's title to uppercase
        game['title'] = game['title'].upper()
        # Add some fictional data for processing demonstration
        game['is_popular'] = self._is_popular(game)
        return game

    def _is_popular(self, game: Dict[str, Any]) -> bool:
        # A game is considered popular if its rating is above 8
        return game.get('rating', 0) > 8

if __name__ == '__main__':
    sample_games = [
        {'title': 'Game One', 'rating': 9},
        {'title': 'Game Two', 'rating': 7},
    ]
    processor = GameProcessor(sample_games)
    results = processor.process()
    print(json.dumps(results, indent=2))