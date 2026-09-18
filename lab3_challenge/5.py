
flights = [
    {"flight_number": "SK142", "destination": "London", "departure_time": "14:30", "gate": "B4", "passengers": 132, "status": "DELAYED"},
    {"flight_number": "LH231", "destination": "Berlin", "departure_time": "15:00", "gate": "A2", "passengers": 96, "status": "ON TIME"},
    {"flight_number": "BA442", "destination": "Manchester", "departure_time": "15:20", "gate": "C1", "passengers": 88, "status": "CANCELLED"},
    {"flight_number": "AF118", "destination": "Paris", "departure_time": "16:10", "gate": "A1", "passengers": 70, "status": "SLIGHT DELAY"},
    {"flight_number": "EK301", "destination": "Dubai", "departure_time": "17:45", "gate": "B2", "passengers": 150, "status": "ON TIME"},
]

search_number = input("Enter flight number: ").strip().upper()

for flight in flights:
    if flight["flight_number"] == search_number:
        print("Destination:", flight["destination"])
        print("Departure:", flight["departure_time"])
        print("Gate:", flight["gate"])
        print("Passengers:", flight["passengers"])
        print("Status:", flight["status"])
        break
else:
    print("Flight not found.")
