from typing import List, Dict, Union, Optional

def calculate_experience_gain(base_xp: int, level_multiplier: float, bonus_modifier: float = 1.0) -> int:
    """Calculates total experience points for quest completion."""
    total = base_xp * level_multiplier * bonus_modifier
    return int(total)

def format_player_stats(stats: Dict[str, Union[int, float]]) -> str:
    """Converts player attribute dictionary to a formatted string."""
    parts = [f"{key.capitalize()}: {value}" for key, value in stats.items()]
    return " | ".join(parts)

def validate_item_rarity(rarity: str, allowed: Optional[List[str]] = None) -> bool:
    """Checks if provided item rarity is within permitted list."""
    if allowed is None:
        allowed = ["common", "rare", "epic", "legendary"]
    return rarity.lower() in allowed

def get_level_threshold(level: int) -> int:
    """Returns the XP requirement for a specific character level."""
    if level <= 0:
        return 0
    return int((level ** 1.5) * 100)

def sanitize_player_input(input_text: str) -> str:
    """Removes whitespace and controls characters from game chat inputs."""
    return " ".join(input_text.split())