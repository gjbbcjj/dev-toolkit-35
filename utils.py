import time
import random
from functools import wraps

def retry(
    max_retries: int = 5,
    base_delay: float = 1.0
):
    """Decorator providing retry logic for network operations.
    Uses exponential backoff with jitter to handle transient failures
    common in gaming network communications like server queries or API calls.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as error:  # Broad for practicality, specify in use
                    if attempt == max_retries - 1:
                        # All retries failed, propagate the error
                        raise
                    # Compute next delay with exponential backoff and jitter
                    delay = base_delay * (2 ** attempt)
                    jitter = random.uniform(0, delay * 0.2)
                    time.sleep(delay + jitter)
        return wrapper
    return decorator

# Sample network operation in gaming toolkit context
@retry(max_retries=3, base_delay=0.5)
def query_game_lobby(lobby_id: str):
    """Mock function representing a network call to fetch lobby data."""
    # Replace with actual requests.get or socket in production
    if random.random() < 0.5:
        raise ConnectionError("Temporary network issue with game lobby")
    return {"lobby_id": lobby_id, "players": [1, 2, 3], "status": "active"}

# This demonstrates the retry in action when run
if __name__ == "__main__":
    import json
    try:
        result = query_game_lobby("test-lobby")
        print(json.dumps(result, indent=2))
    except Exception as err:
        print("Failed to query after retries:", str(err))