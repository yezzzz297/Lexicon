# Part 2 - Numbered departure board

flights = [
    {"number": "SK142", "destination": "London", "departure": "14:30", "gate": "B4", "passengers": 132, "capacity": 180, "delay": 25, "cancelled": False},
    {"number": "LH231", "destination": "Berlin", "departure": "15:00", "gate": "A2", "passengers": 96, "capacity": 150, "delay": 0, "cancelled": False},
    {"number": "BA442", "destination": "Manchester", "departure": "15:20", "gate": "C1", "passengers": 88, "capacity": 140, "delay": 75, "cancelled": True},
    {"number": "AF118", "destination": "Paris", "departure": "16:10", "gate": "A1", "passengers": 0, "capacity": 120, "delay": 10, "cancelled": False},
    {"number": "EK301", "destination": "Dubai", "departure": "17:45", "gate": "B2", "passengers": 150, "capacity": 180, "delay": 0, "cancelled": False},
    {"number": "QR110", "destination": "Doha", "departure": "18:15", "gate": None, "passengers": 42, "capacity": 130, "delay": 30, "cancelled": False},
    {"number": "LX900", "destination": "Zurich", "departure": "19:00", "gate": "A4", "passengers": 110, "capacity": 170, "delay": 5, "cancelled": False},
    {"number": "TG440", "destination": "Bangkok", "departure": "19:50", "gate": "B1", "passengers": 182, "capacity": 200, "delay": 0, "cancelled": False},
    {"number": "AZ210", "destination": "Rome", "departure": "20:40", "gate": "C4", "passengers": 61, "capacity": 140, "delay": 65, "cancelled": False},
    {"number": "KL560", "destination": "Amsterdam", "departure": "21:05", "gate": "B3", "passengers": 134, "capacity": 180, "delay": 0, "cancelled": False},
]

for number, flight in enumerate(flights, start=1):
    gate = flight["gate"]
    if gate is None:
        gate = "not assigned"
    print(number, flight["number"], flight["destination"], flight["departure"], "Gate", gate)
