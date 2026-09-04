class GameDataError(Exception):
    """Base exception class for all gaming data handling errors."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class AssetNotFoundError(GameDataError):
    """Exception raised when a required game asset is missing."""
    def __init__(self, asset_name: str, asset_type: str = "unknown"):
        self.asset_name = asset_name
        self.asset_type = asset_type
        super().__init__(f"Required {asset_type} asset '{asset_name}' could not be located.")


class InvalidSaveError(GameDataError):
    """Exception raised when loading a corrupted or incompatible save file."""
    def __init__(self, save_slot: int, reason: str):
        self.save_slot = save_slot
        self.reason = reason
        super().__init__(f"Failed to load save slot {save_slot}: {reason}")


class ConfigValidationError(GameDataError):
    """Exception raised when game settings or config values fail validation."""
    def __init__(self, setting_name: str, invalid_value: str, expected_range: str):
        self.setting_name = setting_name
        self.invalid_value = invalid_value
        self.expected_range = expected_range
        super().__init__(
            f"Invalid value '{invalid_value}' for setting '{setting_name}'. "
            f"Expected: {expected_range}."
        )