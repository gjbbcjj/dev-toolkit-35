import sys
from validators import validate_user_input

def main_loop():
    while True:
        try:
            user_input = input('Enter a command: ')
            if validate_user_input(user_input):
                process_command(user_input)
            else:
                print('Invalid input, please try again.')
        except (KeyboardInterrupt, SystemExit):
            print('\nExiting the application. Goodbye!')
            sys.exit(0)
        except Exception as e:
            print(f'An error occurred: {e}')


def process_command(command):
    # Here we would handle different commands
    print(f'Processing command: {command}')


if __name__ == '__main__':
    main_loop()