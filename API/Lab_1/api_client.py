
import requests


def get_json(url, params=None, headers=None, timeout=10):
    try:
        response = requests.get(
            url, params=params, headers=headers, timeout=timeout
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("The request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        print("Could not connect. Check the address and your internet connection.")
    except requests.exceptions.HTTPError as error:
        print(f"The server returned HTTP {error.response.status_code}.")
    except requests.exceptions.JSONDecodeError:
        print("The server did not return valid JSON.")
    except requests.exceptions.RequestException:
        print("The request failed. Check the URL and try again.")
    return None
