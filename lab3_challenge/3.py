
flights = [
    {"flight_number": "SK142", "destination": "London", "delay": 25, "cancelled": False},
    {"flight_number": "LH231", "destination": "Berlin", "delay": 0, "cancelled": False},
    {"flight_number": "BA442", "destination": "Manchester", "delay": 90, "cancelled": True},
    {"flight_number": "AF118", "destination": "Paris", "delay": 10, "cancelled": False},
    {"flight_number": "EK301", "destination": "Dubai", "delay": 0, "cancelled": False},
]


def determine_status(flight):
    if flight["cancelled"]:
        return "CANCELLED"
    if flight["delay"] >= 60:
        return "SEVERELY DELAYED"
    if flight["delay"] >= 20:
        return "DELAYED"
    if flight["delay"] >= 1:
        return "SLIGHT DELAY"
    return "ON TIME"


for flight in flights:
    print(f"{flight['flight_number']} - {flight['destination']} - {determine_status(flight)}")
