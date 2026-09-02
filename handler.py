import time
import random
import requests
from typing import Optional, Dict, Any

def perform_with_retry(
    url: str,
    max_retries: int = 5,
    backoff_factor: float = 1.0,
    timeout: int = 10
) -> Optional[Dict[str, Any]]:
    """
    Retry logic for network operations in gaming toolkit.
    Handles transient failures when calling game servers.
    """
    headers = {"User-Agent": "dev-toolkit-35-gaming"}

    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            # Timeout is common in gaming due to server load
            if attempt == max_retries - 1:
                raise
            wait = backoff_factor * (2 ** attempt) + random.uniform(0, 0.5)
            time.sleep(wait)
        except requests.exceptions.ConnectionError:
            if attempt == max_retries - 1:
                raise
            wait = backoff_factor * (2 ** attempt) + random.uniform(0, 0.5)
            time.sleep(wait)
        except requests.exceptions.HTTPError as e:
            # Don't retry on client errors like 404
            if e.response.status_code in [400, 401, 403, 404]:
                raise
            if attempt == max_retries - 1:
                raise
            wait = backoff_factor * (2 ** attempt) + random.uniform(0, 0.5)
            time.sleep(wait)
        except Exception:
            if attempt == max_retries - 1:
                raise
            wait = backoff_factor * (2 ** attempt) + random.uniform(0, 0.5)
            time.sleep(wait)
    return None

# Helper to simulate or wrap for specific gaming ops
def fetch_player_data(player_id: str) -> Optional[Dict[str, Any]]:
    url = f"https://gaming-api.example.com/players/{player_id}"
    return perform_with_retry(url, max_retries=4, backoff_factor=0.5)

# Additional function for post operations if needed
def send_game_event(event_data: Dict[str, Any]) -> bool:
    # Example for posting, but using get for simplicity
    # In real, implement post
    url = "https://gaming-api.example.com/events"
    try:
        result = perform_with_retry(url, max_retries=3)
        return result is not None
    except:
        return False