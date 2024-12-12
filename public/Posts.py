import httpx

def fetch_all(base_url: str):
    """Fetch all posts."""
    response = httpx.get(f"{base_url}/posts")
    response.raise_for_status()
    return response.json()

def fetch_by_id(base_url: str, post_id: int):
    """Fetch a post by ID."""
    response = httpx.get(f"{base_url}/posts/{post_id}")
    response.raise_for_status()
    return response.json()
