import math
from typing import Tuple

def calculate_distance_3d(point_a: Tuple[float, float, float], point_b: Tuple[float, float, float]) -> float:
    """Calculate the Euclidean distance between two 3D points."""
    return math.sqrt(
        (point_a[0] - point_b[0]) ** 2 +
        (point_a[1] - point_b[1]) ** 2 +
        (point_a[2] - point_b[2]) ** 2
    )

def is_within_bounds(position: Tuple[float, float, float], min_bounds: Tuple[float, float, float], max_bounds: Tuple[float, float, float]) -> bool:
    """Check if a 3D position is within specified bounding box limits."""
    return (
        min_bounds[0] <= position[0] <= max_bounds[0] and
        min_bounds[1] <= position[1] <= max_bounds[1] and
        min_bounds[2] <= position[2] <= max_bounds[2]
    )

def calculate_xp_for_level(level: int, base_xp: int = 100, exponent: float = 1.5) -> int:
    """Determine the total XP required to reach a specific level."""
    if level <= 1:
        return 0
    return int(base_xp * (level ** exponent))

def lerp(start: float, end: float, alpha: float) -> float:
    """Linearly interpolate between start and end values by alpha."""
    alpha = max(0.0, min(1.0, alpha))
    return start + alpha * (end - start)