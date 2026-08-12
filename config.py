import json
from pathlib import Path

class ConfigLoader:
    def __init__(self, default_config_path, user_config_path):
        self.default_config_path = Path(default_config_path)
        self.user_config_path = Path(user_config_path)
        self.config = self.load_config()

    def load_config(self):
        default_config = self.load_json(self.default_config_path)
        user_config = self.load_json(self.user_config_path)
        return self.merge_configs(default_config, user_config)

    def load_json(self, path):
        if path.exists():
            with open(path) as file:
                return json.load(file)
        return {}

    def merge_configs(self, default, user):
        merged = default.copy()
        merged.update(user)
        return merged

if __name__ == '__main__':
    loader = ConfigLoader('default_config.json', 'user_config.json')
    print(loader.config)