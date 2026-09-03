from typing import Final, Dict, List

# Configuration constants for dev-toolkit-35
MAX_RETRY_ATTEMPTS: Final[int] = 5
DEFAULT_TIMEOUT: Final[float] = 30.5

# Supported gaming platform identifiers
SUPPORTED_PLATFORMS: Final[List[str]] = ['steam', 'epic', 'gog', 'origin']

# Mapping for game resource status codes
RESOURCE_STATUS_MAP: Final[Dict[int, str]] = {
    200: 'READY',
    202: 'PROCESSING',
    404: 'NOT_FOUND',
    500: 'SERVER_ERROR'
}

class EngineConstants:
    """Container for engine-specific operational limits."""
    FRAME_RATE_LIMIT: Final[int] = 144
    MAX_TEXTURE_SIZE: Final[int] = 4096
    DEFAULT_ENCODING: Final[str] = 'utf-8'

def get_platform_timeout(platform: str) -> float:
    """Return timeout duration for a given gaming platform."""
    return DEFAULT_TIMEOUT if platform in SUPPORTED_PLATFORMS else 60.0