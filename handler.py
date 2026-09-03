import time
import functools
import logging

logger = logging.getLogger('dev-toolkit-35')

def retry_network_op(retries=3, delay=1.0, backoff=2.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == retries - 1:
                        logger.error(f'Operation failed after {retries} attempts')
                        raise
                    logger.warning(f'Attempt {attempt + 1} failed, retrying in {current_delay}s...')
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_network_op(retries=3, delay=2.0)
def fetch_game_data(endpoint):
    """Simulated network call to game server."""
    # Example implementation for dev-toolkit-35
    print(f'Fetching data from {endpoint}...')
    return {'status': 'success', 'data': 'game_state_payload'}