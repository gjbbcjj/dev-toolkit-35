import time
import requests


def retry_request(url, max_retries=3, delay=2, backoff=2):
    """Perform a network request with retry logic."""
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status codes
            return response.json()  # Return the JSON response if successful
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            attempt += 1
            time.sleep(delay)
            delay *= backoff  # Increase delay exponentially
    raise Exception(f"Failed to fetch data from {url} after {max_retries} attempts.")


# Example of using the retry logic
if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry_request(url)
        print(data)
    except Exception as e:
        print(e)