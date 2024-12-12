from dotenv import load_dotenv
import os

def load_config():
    load_dotenv()
    return {
        "BASE_URL": os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
    }
