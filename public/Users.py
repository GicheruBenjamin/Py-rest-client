import httpx

def fetch_all(base_url: str):
    """Fetch all users."""
    response = httpx.get(f"{base_url}/users")
    response.raise_for_status()
    return response.json()

def fetch_by_id(base_url: str, user_id: int):
    """Fetch a user by ID."""
    response = httpx.get(f"{base_url}/users/{user_id}")
    response.raise_for_status()
    return response.json()
