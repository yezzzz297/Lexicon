flights = [
    {"flight_number": "SK142", "destination": "London", "departure_time": "14:30", "gate": "B4", "passengers": 132, "delay": 25, "cancelled": False},
    {"flight_number": "LH231", "destination": "Berlin", "departure_time": "15:00", "gate": "A2", "passengers": 96, "delay": 0, "cancelled": False},
    {"flight_number": "BA442", "destination": "Manchester", "departure_time": "15:20", "gate": None, "passengers": 88, "delay": 90, "cancelled": False},
    {"flight_number": "AF118", "destination": "Paris", "departure_time": "16:10", "gate": "A1", "passengers": 0, "delay": 10, "cancelled": False},
    {"flight_number": "EK301", "destination": "Dubai", "departure_time": "17:45", "gate": "B2", "passengers": 150, "delay": 0, "cancelled": True},
    {"flight_number": "QR110", "destination": "Doha", "departure_time": "18:15", "gate": "C3", "passengers": 42, "delay": 30, "cancelled": False},
]

for flight in flights:
    gate = flight["gate"] if flight["gate"] else "Gate not assigned"
    if flight["cancelled"]:
        status = "CANCELLED"
    elif flight["delay"] >= 60:
        status = "SEVERELY DELAYED"
    elif flight["delay"] >= 20:
        status = "DELAYED"
    elif flight["delay"] >= 1:
        status = "SLIGHT DELAY"
    else:
        status = "ON TIME"

    print(f"{flight['flight_number']} - {flight['destination']} - {flight['departure_time']} - {gate} - {status} - {flight['passengers']} passengers")

active_flights = []
total_passengers = 0

for flight in flights:
    if flight["cancelled"]:
        continue
    if flight["passengers"] == 0:
        continue

    active_flights.append(flight)
    total_passengers += flight["passengers"]


average = total_passengers / len(active_flights) if active_flights else 0
print("Average passengers for active flights:", average)
