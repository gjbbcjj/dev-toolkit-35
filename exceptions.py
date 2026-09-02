import json
import os
from typing import Any, Dict, Optional

class ConfigLoader:
    def __init__(self, config_path: str, defaults: Optional[Dict[str, Any]] = None) -> None:
        self.config_path = config_path
        self.defaults = defaults or {}
        self.config: Dict[str, Any] = self._load()

    def _load(self) -> Dict[str, Any]:
        config = self.defaults.copy()
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    loaded = json.load(f)
                    if isinstance(loaded, dict):
                        config.update(loaded)
            except (json.JSONDecodeError, IOError, OSError):
                # fall back to defaults on error
                config = self.defaults.copy()
        return config

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        return self.config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self.config[key] = value

    def save(self) -> None:
        try:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=4)
        except (IOError, OSError):
            pass  # or handle error, but for now

    def reload(self) -> None:
        self.config = self._load()

# For gaming dev toolkit
if __name__ == "__main__":
    default_settings = {
        "window_width": 1280,
        "window_height": 720,
        "fps_limit": 60,
        "sound_enabled": True,
        "difficulty": "medium"
    }
    config = ConfigLoader("settings.json", default_settings)
    print(config.get("fps_limit"))
    config.set("difficulty", "hard")
    config.save()