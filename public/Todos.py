import httpx

def fetch_all(base_url: str):
    """Fetch all todos."""
    response = httpx.get(f"{base_url}/todos")
    response.raise_for_status()
    return response.json()

def fetch_by_id(base_url: str, todo_id: int):
    """Fetch a todo by ID."""
    response = httpx.get(f"{base_url}/todos/{todo_id}")
    response.raise_for_status()
    return response.json()
