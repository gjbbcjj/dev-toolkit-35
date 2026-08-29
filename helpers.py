import random
from typing import Dict, List, Tuple
def roll_dice(sides: int = 6, count: int = 1) -> List[int]:
    """Roll dice and return list of results.
    Args:
        sides: Number of sides per die.
        count: Number of dice to roll.
    Returns:
        List of integers representing each roll.
    """
    return [random.randint(1, sides) for _ in range(count)]
def calculate_experience(level: int) -> int:
    """Calculate required experience for next level.
    Args:
        level: Current player level.
    Returns:
        Integer experience points needed.
    """
    return level * 100 + 50
def add_item(inventory: Dict[str, int], item: str, quantity: int = 1) -> Dict[str, int]:
    """Add item to inventory dictionary.
    Args:
        inventory: Existing inventory.
        item: Item name to add.
        quantity: Amount to add.
    Returns:
        Updated inventory dictionary.
    """
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    return inventory
def check_level_up(current_xp: int, current_level: int) -> Tuple[bool, int]:
    """Determine if level up is possible.
    Args:
        current_xp: Current experience total.
        current_level: Current level.
    Returns:
        Tuple with boolean for level up and new level.
    """
    needed: int = calculate_experience(current_level)
    if current_xp >= needed:
        return True, current_level + 1
    return False, current_level
class Player:
    """Simple player class for game tracking."""
    def __init__(self, name: str, level: int = 1) -> None:
        """Create player instance.
        Args:
            name: Player identifier.
            level: Initial level.
        """
        self.name: str = name
        self.level: int = level
        self.xp: int = 0
        self.inventory: Dict[str, int] = {}
    def gain_xp(self, amount: int) -> bool:
        """Increase experience and possibly level up.
        Args:
            amount: XP points to add.
        Returns:
            Whether a level up occurred.
        """
        self.xp += amount
        leveled_up, new_level = check_level_up(self.xp, self.level)
        if leveled_up:
            self.level = new_level
            self.xp = 0
            return True
        return False
    def add_to_inventory(self, item: str, quantity: int = 1) -> None:
        """Add items to player inventory.
        Args:
            item: Name of item.
            quantity: Number of items.
        """
        self.inventory = add_item(self.inventory, item, quantity)