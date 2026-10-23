import os
import requests
from dotenv import load_dotenv
from api_client import get_json

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
key = os.getenv("API_KEY")
BASE = "http://127.0.0.1:8000"

print("All movies:")
print(get_json(f"{BASE}/movies"))

print("Missing movie:")
get_json(f"{BASE}/movies/999999")

new_movie = {"title": "Interstellar", "director": "Christopher Nolan", "year": 2014}

print("POST without a key:")
try:
    response = requests.post(f"{BASE}/movies", json=new_movie, timeout=5)
    print("Status:", response.status_code)
    print(response.json())
    response.raise_for_status()
except requests.exceptions.HTTPError:
    print("401 is expected because no key was sent.")
except requests.exceptions.RequestException as error:
    print("Request failed:", type(error).__name__)

print("POST with a key:")
if not key:
    print("Add API_KEY to .env first.")
else:
    try:
        response = requests.post(
            f"{BASE}/movies", json=new_movie,
            headers={"X-API-Key": key}, timeout=5,
        )
        print("Status:", response.status_code)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.RequestException as error:
        print("Request failed:", type(error).__name__)
