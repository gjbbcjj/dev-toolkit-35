import random
import sys

class Game:
    def __init__(self):
        self.running = True

    def start(self):
        print('Game started!')
        while self.running:
            user_input = input('Enter a number (1-10) or type "exit" to quit: ')
            self.process_input(user_input)

    def process_input(self, user_input):
        if user_input.lower() == 'exit':
            self.running = False
            print('Exiting game...')
        else:
            try:
                number = int(user_input)
                if 1 <= number <= 10:
                    print(f'You entered: {number}')
                else:
                    print('Input should be between 1 and 10.')
            except ValueError:
                print('Invalid input; please enter a number.')

if __name__ == '__main__':
    game = Game()
    game.start()