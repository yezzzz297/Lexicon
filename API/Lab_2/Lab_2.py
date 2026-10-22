from api_client import get_json


def find_city(name):
    data = get_json(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": name, "count": 1},
    )
    if data is None:
        return None
    print(data)
    cities = data.get("results", [])
    if not cities:
        print("City not found. Try another name.")
        return None
    city = cities[0]
    print("Latitude:", city["latitude"])
    print("Longitude:", city["longitude"])
    return city


def get_weather(lat, lon):
    data = get_json(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,wind_speed_10m",
        },
    )
    if data is not None:
        print(data)
    return data



name = input("Enter a city: ").strip()
if not name:
    print("Please enter a city name.")
else:
    city = find_city(name)
    if city is not None:
        weather = get_weather(city["latitude"], city["longitude"])
        if weather is not None:
            current = weather["current"]
            units = weather["current_units"]
            print(
                f"{city['name']}, {city.get('country', '')}: "
                f"{current['temperature_2m']}{units['temperature_2m']}, "
                f"wind {current['wind_speed_10m']} {units['wind_speed_10m']}"
            )
