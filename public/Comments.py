
import httpx

def fetch_all(base_url: str):
    """Fetch all comments."""
    response = httpx.get(f"{base_url}/comments")
    response.raise_for_status()
    return response.json()

def fetch_by_id(base_url: str, comment_id: int):
    """Fetch a comment by ID."""
    response = httpx.get(f"{base_url}/comments/{comment_id}")
    response.raise_for_status()
    return response.json()
