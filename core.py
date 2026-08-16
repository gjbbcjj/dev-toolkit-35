import random
import time


def random_seed(seed: int) -> None:
    """Set the random seed for reproducibility."""
    random.seed(seed)


def roll_dice(sides: int = 6, rolls: int = 1) -> list:
    """Roll a dice with the specified number of sides a given number of times."""
    return [random.randint(1, sides) for _ in range(rolls)]


def wait_for_seconds(seconds: float) -> None:
    """Pause execution for a given number of seconds."""
    time.sleep(seconds)


def generate_random_string(length: int = 10) -> str:
    """Generate a random alphanumeric string of specified length."""
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for _ in range(length))


def limit_range(value: int, min_value: int, max_value: int) -> int:
    """Limit a value to be within a specified range."""
    return max(min(value, max_value), min_value)