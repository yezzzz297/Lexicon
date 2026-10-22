import json
import os
import time
from api_client import get_json

cache_file = os.path.join(os.path.dirname(__file__), "weather_cache.json")
name = input("Enter a city: ").strip().lower()
data = None

# Reading saved weather is faster than calling the API again.
# Fewer requests also help us avoid API rate limits.
if name and os.path.exists(cache_file):
    age = time.time() - os.path.getmtime(cache_file)
    if 0 <= age < 600:
        try:
            with open(cache_file) as file:
                saved = json.load(file)
            if saved["query"] == name:
                data = saved
                print("Using cached weather. No API calls needed.")
        except (OSError, ValueError, KeyError, TypeError):
            print("Could not read the cache. Trying the API.")

if not name:
    print("Please enter a city name.")
elif data is None:
    result = get_json(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": name, "count": 1},
    )
    if result is not None:
        if not result.get("results"):
            print("City not found.")
        else:
            city = result["results"][0]
            weather = get_json(
                "https://api.open-meteo.com/v1/forecast",
                params={
                    "latitude": city["latitude"],
                    "longitude": city["longitude"],
                    "current": "temperature_2m,wind_speed_10m",
                },
            )
            if weather is not None:
                data = {"query": name, "city": city, "weather": weather}
                try:
                    with open(cache_file, "w") as file:
                        json.dump(data, file, indent=2)
                    print("Saved weather to cache.")
                except OSError:
                    print("Could not save the cache.")

if data is not None:
    city = data["city"]
    current = data["weather"]["current"]
    units = data["weather"]["current_units"]
    print(
        f"{city['name']}, {city.get('country', '')}: "
        f"{current['temperature_2m']}{units['temperature_2m']}, "
        f"wind {current['wind_speed_10m']} {units['wind_speed_10m']}"
    )
