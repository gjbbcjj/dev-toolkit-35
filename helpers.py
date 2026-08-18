import random
import math

def generate_random_number(min_value: int, max_value: int) -> int:
    """
    Generate a random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def calculate_distance(point_a: tuple, point_b: tuple) -> float:
    """
    Calculate the Euclidean distance between two points.
    """
    return math.sqrt((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2)


def is_within_bounds(position: tuple, bounds: tuple) -> bool:
    """
    Check if a given position is within specified bounds.
    """
    return bounds[0] <= position[0] <= bounds[2] and bounds[1] <= position[1] <= bounds[3]


def clamp_value(value: float, min_value: float, max_value: float) -> float:
    """
    Clamp a value to be within min_value and max_value.
    """
    return max(min_value, min(value, max_value))


def random_choice_from_list(items: list) -> any:
    """
    Return a random element from a non-empty list.
    """
    if not items:
        raise ValueError('The list is empty')
    return random.choice(items)