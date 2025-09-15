import requests
import sys
import os
import json

def fetch_json(url: str):
    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        print( json.dumps(data, indent=2))
        
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except ValueError as e:
        print(f"Invalid JSON: {e}")

if __name__ == "__main__":
    url = os.environ.get("TARGET_URL") or (sys.argv[1] if len(sys.argv) > 1 else None)
    if url is None or not url:
        url = "https://jsonplaceholder.typicode.com/todos/1"
    fetch_json(url)

