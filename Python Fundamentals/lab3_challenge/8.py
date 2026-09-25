# Part 8 - All six menu choices

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

for flight in flights:
    if flight["cancelled"]:
        flight["status"] = "CANCELLED"
    elif flight["delay"] >= 60:
        flight["status"] = "SEVERELY DELAYED"
    elif flight["delay"] >= 20:
        flight["status"] = "DELAYED"
    elif flight["delay"] > 0:
        flight["status"] = "SLIGHT DELAY"
    else:
        flight["status"] = "ON TIME"

    if flight["gate"] is None:
        flight["gate_text"] = "Gate not assigned"
    else:
        flight["gate_text"] = "Gate " + flight["gate"]

cancelled = 0
delayed = 0
on_time = 0
passengers = 0
busiest = None
full_flights = []

for flight in flights:
    if flight["cancelled"]:
        cancelled += 1
        continue
    passengers += flight["passengers"]
    if flight["delay"] > 0:
        delayed += 1
    else:
        on_time += 1
    if busiest is None or flight["passengers"] > busiest["passengers"]:
        busiest = flight
    if flight["passengers"] > flight["capacity"] * 0.8:
        full_flights.append(flight)

# Cancelled flights count as scheduled but carry zero passengers today.
average = 0
if len(flights) > 0:
    average = passengers / len(flights)

while True:
    print("1. All flights")
    print("2. Delayed flights")
    print("3. Cancelled flights")
    print("4. Search")
    print("5. Statistics")
    print("6. Quit")
    choice = input("Choose: ")

    if choice == "1":
        for number, flight in enumerate(flights, start=1):
            print(number, flight["number"], flight["destination"], flight["departure"],
                  flight["gate_text"], flight["status"])

    elif choice == "2":
        for flight in flights:
            if flight["delay"] > 0 and not flight["cancelled"]:
                print(flight["number"], flight["destination"], flight["delay"])
    elif choice == "3":
        for flight in flights:
            if flight["cancelled"]:
                print(flight["number"], flight["destination"], flight["status"])
    elif choice == "4":
        search = input("Flight number: ").strip().upper()
        found = False
        for flight in flights:
            if flight["number"] == search:
                print("Destination:", flight["destination"])
                print("Departure:", flight["departure"])
                print(flight["gate_text"])
                print("Passengers:", flight["passengers"])
                print("Status:", flight["status"])
                found = True
                break
        if not found:
            print("Flight not found.")
    elif choice == "5":
        print("Scheduled flights:", len(flights))
        print("Cancelled:", cancelled)
        print("Delayed:", delayed)
        print("On time:", on_time)
        print("Passengers today:", passengers)
        print("Average per scheduled flight:", round(average, 2))
        if busiest is not None:
            print("Busiest:", busiest["number"], busiest["destination"], busiest["passengers"])
        print("Flights above 80% capacity:", len(full_flights))
    elif choice == "6":
        print("Goodbye")
        break
    else:
        print("Invalid choice")
