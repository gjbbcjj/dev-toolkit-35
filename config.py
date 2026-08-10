import json
import os

class ConfigLoader:
    def __init__(self, default_config_path='default_config.json', user_config_path='user_config.json'):
        self.default_config_path = default_config_path
        self.user_config_path = user_config_path
        self.config = self.load_config()

    def load_config(self):
        # Load default configuration
        default_config = self.load_json(self.default_config_path)
        # Load user configuration if it exists
        user_config = self.load_json(self.user_config_path)
        # Merge configurations, user config takes precedence
        return {**default_config, **user_config}

    def load_json(self, path):
        if os.path.exists(path):
            with open(path, 'r') as file:
                return json.load(file)
        return {}

    def get(self, key, default=None):
        return self.config.get(key, default)

if __name__ == '__main__':
    config_loader = ConfigLoader()
    print(config_loader.config)  # Debug print of the configuration
