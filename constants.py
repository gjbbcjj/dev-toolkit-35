import time
import random

MAX_RETRIES = 5
DELAY = 2  # seconds

class NetworkError(Exception):
    pass

def retry_on_failure(func):
    """
    Decorator to retry a function call on failure.
    """  
    def wrapper(*args, **kwargs):
        for attempt in range(MAX_RETRIES):
            try:
                return func(*args, **kwargs)
            except NetworkError as e:
                if attempt < MAX_RETRIES - 1:
                    wait_time = DELAY + random.uniform(0, 1)  # jitter
                    time.sleep(wait_time)
                else:
                    raise e  # re-raise the last exception
    return wrapper

@retry_on_failure
def fetch_data_from_server(url):
    """
    Simulates a network operation to fetch data.
    Raises NetworkError randomly to simulate failure.
    """  
    if random.random() < 0.7:  # 70% chance to fail
        raise NetworkError('Failed to connect')
    return { 'data': 'Sample data from {}'.format(url) }
