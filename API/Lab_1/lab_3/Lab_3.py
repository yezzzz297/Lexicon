import os
from getpass import getpass
import requests
from dotenv import load_dotenv
from api_client import get_json

# Tasks 1-2: put your token in the ignored .env file.
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
token = os.getenv("GITHUB_TOKEN", "").strip()

if not token:
    token = getpass("Paste your GitHub token (hidden, Enter to cancel): ").strip()

if not token:
    print("No token provided. Create your token using Lab 3 Task 1, then run again.")
else:
    username = input("GitHub username: ").strip()
    if not username:
        print("Please enter a username.")
    else:
        # Task 3: get the five latest pushed repositories.
        url = f"https://api.github.com/users/{username}/repos"
        headers = {"Authorization": f"Bearer {token}"}
        repos = get_json(url, params={"sort": "pushed", "per_page": 5}, headers=headers)
        if repos is not None:
            for repo in repos:
                print(repo["name"])
            if not repos:
                print("No public repositories found.")

        # Task 4: compare the limits with and without a token.
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            print("Without token:", response.headers.get("X-RateLimit-Limit"))

            response = requests.get(url, headers=headers, timeout=5)
            response.raise_for_status()
            print("With token:", response.headers.get("X-RateLimit-Limit"))
        except requests.exceptions.RequestException as error:
            print("Could not check the limits:", type(error).__name__)

        # Task 5: change one character in a copy of the token.
        if token[-1] == "x":
            wrong_token = token[:-1] + "y"
        else:
            wrong_token = token[:-1] + "x"

        try:
            response = requests.get(
                "https://api.github.com/user",
                headers={"Authorization": f"Bearer {wrong_token}"},
                timeout=5,
            )
            print("Wrong token status:", response.status_code)
            print(response.json())
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            print("401: missing or invalid authentication. 403: access forbidden.")
        except requests.exceptions.RequestException as error:
            print("Token test failed:", type(error).__name__)

        print("Check that .env is ignored, then delete your token on GitHub.")
