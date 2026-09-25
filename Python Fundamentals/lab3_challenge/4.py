# Part 4 - Calculate all eight statistics

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

print("Scheduled flights:", len(flights))
print("Cancelled:", cancelled)
print("Delayed:", delayed)
print("On time:", on_time)
print("Passengers today:", passengers)
print("Average per scheduled flight:", round(average, 2))
if busiest is not None:
    print("Busiest:", busiest["number"], busiest["destination"], busiest["passengers"])
print("Flights above 80% capacity:", len(full_flights))
