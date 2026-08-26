"""Gaming configuration constants for dev-toolkit-35."""

from typing import Final, Dict, List

# Maximum number of players allowed in a standard lobby session
MAX_LOBBY_SIZE: Final[int] = 16

# Default network timeout duration measured in seconds
DEFAULT_TIMEOUT: Final[float] = 5.0

# Supported graphics rendering APIs for the game engine
SUPPORTED_APIS: Final[List[str]] = ["DirectX12", "Vulkan", "OpenGL"]

# Mapping of difficulty levels to enemy health multipliers
DIFFICULTY_MULTIPLIERS: Final[Dict[str, float]] = {
    "casual": 0.75,
    "normal": 1.00,
    "hardcore": 1.50,
    "nightmare": 2.00,
}

def get_multiplier(difficulty: str) -> float:
    """Retrieve the health multiplier for a given difficulty level.
    
    Args:
        difficulty: The string identifier of the difficulty level.
        
    Returns:
        The float multiplier associated with the difficulty, defaulting to normal (1.0).
    """
    return DIFFICULTY_MULTIPLIERS.get(difficulty.lower(), 1.0)
