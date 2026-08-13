import json

class Config:
    def __init__(self, filepath):
        self.filepath = filepath
        self.config_data = self.load_config()

    def load_config(self):
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading config: {e}")
            return {}

    def get(self, key, default=None):
        return self.config_data.get(key, default)

    def set(self, key, value):
        self.config_data[key] = value
        self.save_config()

    def save_config(self):
        try:
            with open(self.filepath, 'w') as file:
                json.dump(self.config_data, file, indent=4)
        except IOError as e:
            print(f"Error saving config: {e}")

# Example usage
if __name__ == '__main__':
    config = Config('game_config.json')
    print(config.get('difficulty', 'normal'))
    config.set('difficulty', 'hard')