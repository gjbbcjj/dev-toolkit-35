"""Helper functions for common gaming operations."""

import math
import random
from typing import Tuple, List, Any

def calculate_distance(pos1: Tuple[float, float], pos2: Tuple[float, float]) -> float:
    """Calculate Euclidean distance between two points."""
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    return math.sqrt(dx * dx + dy * dy)

def clamp(value: float, min_val: float, max_val: float) -> float:
    """Restrict value to the range [min_val, max_val]."""
    return max(min_val, min(max_val, value))

def lerp(a: float, b: float, t: float) -> float:
    """Linear interpolation from a to b by factor t."""
    return a + (b - a) * t

def weighted_choice(options: List[Tuple[Any, float]]) -> Any:
    """Return random item weighted by second tuple element."""
    total = sum(w for _, w in options)
    r = random.random() * total
    upto = 0.0
    for item, weight in options:
        if upto + weight >= r:
            return item
        upto += weight
    return options[-1][0]

def format_score(score: int) -> str:
    """Return score as string with commas."""
    return f"{score:,}"

def get_exp_for_level(level: int) -> int:
    """Compute experience needed for next level."""
    return int(100 * level ** 1.5)

def rects_overlap(r1: Tuple[float, float, float, float], r2: Tuple[float, float, float, float]) -> bool:
    """Detect overlap of two rectangles (x, y, width, height)."""
    x1, y1, w1, h1 = r1
    x2, y2, w2, h2 = r2
    return (x1 < x2 + w2 and x1 + w1 > x2 and
            y1 < y2 + h2 and y1 + h1 > y2)

def pick_event(events: List[str]) -> str:
    """Select random event from list."""
    if not events:
        return ""
    return random.choice(events)