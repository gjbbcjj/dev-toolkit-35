import random

def calculate_critical_hit(base_damage: float, crit_chance: float, crit_multiplier: float = 1.5) -> float:
    """Calculate final damage considering critical hit chance and multiplier."""
    if not (0.0 <= crit_chance <= 1.0):
        raise ValueError("Crit chance must be between 0.0 and 1.0")
    
    is_crit = random.random() <= crit_chance
    if is_crit:
        return base_damage * crit_multiplier
    return base_damage

def interpolate_health(current_hp: float, target_hp: float, alpha: float) -> float:
    """Smoothly interpolate health for UI health bar animations."""
    alpha = max(0.0, min(1.0, alpha))
    return current_hp + (target_hp - current_hp) * alpha

def roll_loot_drop(loot_table: dict[str, float]) -> str | None:
    """Determine item drop based on weighted probability table."""
    total_weight = sum(loot_table.values())
    if total_weight <= 0:
        return None
        
    roll = random.uniform(0, total_weight)
    current_weight = 0.0
    
    for item, weight in loot_table.items():
        current_weight += weight
        if roll <= current_weight:
            return item
            
    return None