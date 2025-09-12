import requests

def fetch_json(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        print(data)
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except ValueError as e:
        print(f"Invalid JSON: {e}")

if __name__ == "__main__":
    # Example: JSON placeholder test API
    url = "https://jsonplaceholder.typicode.com/todos/1"
    fetch_json(url)

