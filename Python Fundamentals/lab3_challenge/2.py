
flights = [
    {"flight_number": "SK142", "destination": "London", "departure_time": "14:30", "gate": "B4"},
    {"flight_number": "LH231", "destination": "Berlin", "departure_time": "15:00", "gate": "A2"},
    {"flight_number": "BA442", "destination": "Manchester", "departure_time": "15:20", "gate": "C1"},
    {"flight_number": "AF118", "destination": "Paris", "departure_time": "16:10", "gate": "A1"},
    {"flight_number": "EK301", "destination": "Dubai", "departure_time": "17:45", "gate": "B2"},
    {"flight_number": "QR110", "destination": "Doha", "departure_time": "18:15", "gate": "C3"},
    {"flight_number": "LX900", "destination": "Zurich", "departure_time": "19:00", "gate": "A4"},
    {"flight_number": "TG440", "destination": "Bangkok", "departure_time": "19:50", "gate": "B1"},
    {"flight_number": "AZ210", "destination": "Rome", "departure_time": "20:40", "gate": "C4"},
    {"flight_number": "KL560", "destination": "Amsterdam", "departure_time": "21:05", "gate": "B3"},
]

for index, flight in enumerate(flights, start=1):
    print(f"{index}. {flight['flight_number']} - {flight['destination']} - {flight['departure_time']} - Gate {flight['gate']}")
