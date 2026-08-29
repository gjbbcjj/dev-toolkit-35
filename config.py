import json
import os
from typing import Any, Dict

DEFAULTS = {
    "window": {
        "width": 800,
        "height": 600,
        "fullscreen": False
    },
    "game": {
        "fps": 60,
        "difficulty": "medium"
    },
    "audio": {
        "volume": 100
    }
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Load config from JSON file or use defaults if not found."""
    config = DEFAULTS.copy()
    if os.path.isfile(filepath):
        try:
            with open(filepath, "r") as file:
                loaded = json.load(file)
            config = merge_dicts(config, loaded)
        except (json.JSONDecodeError, OSError):
            pass  # fall back to defaults
    return config

def merge_dicts(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """Deep merge override into base."""
    for key, value in override.items():
        if key in base and isinstance(base[key], dict) and isinstance(value, dict):
            base[key] = merge_dicts(base[key], value)
        else:
            base[key] = value
    return base

class ConfigLoader:
    """Configuration loader with support for defaults and overrides."""
    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.config = load_config(filepath)

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a nested value using dot-separated key."""
        keys = key.split(".")
        value = self.config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value

    def update(self, key: str, value: Any) -> None:
        """Update a nested value."""
        keys = key.split(".")
        current = self.config
        for k in keys[:-1]:
            if k not in current or not isinstance(current[k], dict):
                current[k] = {}
            current = current[k]
        current[keys[-1]] = value

    def save(self) -> None:
        """Save current config to file."""
        try:
            with open(self.filepath, "w") as file:
                json.dump(self.config, file, indent=4)
        except OSError:
            pass