import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, delay=1):
    """Perform a GET request with retry logic."""
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return JSON data if successful
        except RequestException as e:
            print(f'Attempt {attempt + 1} failed: {e}')
            if attempt < max_retries - 1:
                time.sleep(delay)  # Wait before retrying
            else:
                raise  # Reraise the last exception if max retries reached

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry_request(url)
        print('Data retrieved:', data)
    except Exception as e:
        print('Failed to retrieve data:', e)