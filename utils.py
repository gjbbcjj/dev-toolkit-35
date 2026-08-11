import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, backoff_factor=0.3):
    """Perform a request with retry logic.

    Args:
        url (str): The URL to request.
        max_retries (int): Maximum number of retry attempts.
        backoff_factor (float): A backoff factor for delay between retries.

    Returns:
        Response: The response object if the request is successful.
    """
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except RequestException as e:
            retries += 1
            wait = backoff_factor * (2 ** (retries - 1))
            print(f"Warning: Request failed with {e}. Retrying in {wait:.1f} seconds...")
            time.sleep(wait)
    raise RequestException(f"Failed to retrieve data from {url} after {max_retries} attempts")