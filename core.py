import time
import numpy as np

class Game:
    def __init__(self, players):
        self.players = players
        self.scores = np.zeros(len(players))

    def play_round(self):
        for idx, player in enumerate(self.players):
            # Simulate player action
            action_time = time.perf_counter()
            self.scores[idx] += player.take_action()
            action_duration = time.perf_counter() - action_time
            self.log_action_time(idx, action_duration)

    def log_action_time(self, player_idx, duration):
        print(f'Player {player_idx} took {duration:.4f} seconds.')

    def get_scores(self):
        return self.scores

class Player:
    def take_action(self):
        # Simulate a time-consuming action
        time.sleep(np.random.rand() * 0.1)
        return np.random.randint(1, 10)

if __name__ == '__main__':
    players = [Player() for _ in range(3)]
    game = Game(players)
    for _ in range(5):
        game.play_round()
    print('Final scores:', game.get_scores())