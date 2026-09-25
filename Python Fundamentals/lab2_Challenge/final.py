# Final challenge - Complete conference

speakers = ["Ada", "Sarah", "Abel", "David", "Anna"]
rooms = ["A", "B", "C", "D"]
participants = ["Anna", "David", "Sara", "Leo", "Mia", "Noah", "Nora", "Oscar", "Lina", "Yusuf"]
topics = {"Python", "Web", "AI", "Security", "Testing"}
hours = ("09:00", "17:00")

sessions = [
    {"title": "Python", "speaker": "Ada", "room": "A",
     "start": "09:00", "duration": 60, "topic": "AI", "capacity": 40},
    {"title": "Java", "speaker": "Sarah", "room": "B",
     "start": "09:00", "duration": 60, "topic": "Web", "capacity": 30},
    {"title": "AI Basics", "speaker": "Abel", "room": "C",
     "start": "10:00", "duration": 60, "topic": "AI", "capacity": 25},
    {"title": "Computer Safety", "speaker": "David", "room": "D",
     "start": "10:00", "duration": 60, "topic": "Security", "capacity": 20},
    {"title": "Testing", "speaker": "Anna", "room": "A",
     "start": "11:00", "duration": 45, "topic": "Testing", "capacity": 40},
    {"title": "Python Lists", "speaker": "Ada", "room": "B",
     "start": "11:00", "duration": 45, "topic": "Python", "capacity": 30},
    {"title": "Web Basics", "speaker": "Sarah", "room": "C",
     "start": "13:00", "duration": 60, "topic": "Web", "capacity": 25},
    {"title": "Practice", "speaker": "Anna", "room": "D",
     "start": "14:00", "duration": 60, "topic": "Testing", "capacity": 20}
]

conference = {
    "name": "Tech Together", "hours": hours,
    "sessions": sessions, "speakers": speakers, "rooms": rooms,
    "participants": participants, "topics": topics,
    "workshops": {"A": {"Anna", "David", "Sara"}, "B": {"Sara", "Leo"}}
}

# Read ten values from the conference.
print(conference["name"])
print(conference["hours"][0])
print(conference["hours"][1])
print(conference["sessions"][0]["title"])
print(conference["sessions"][0]["speaker"])
print(conference["sessions"][-1]["room"])
print(conference["speakers"][1])
print(conference["rooms"][0])
print(conference["participants"][0])
print(conference["workshops"]["A"])

# Make five changes.
conference["name"] = "Tech Together 2026"
conference["sessions"][0]["difficulty"] = "Beginner"
conference["participants"].append("Ruth")
conference["participants"].remove("Yusuf")
conference["workshops"]["A"].add("Ruth")
print("Updated conference:", conference)

# Lists: keep sessions and participants in order and allow changes.
# Dictionaries: give details clear names, such as title and speaker.
# Tuples: group fixed opening and closing times.
# Sets: keep topics and workshop members unique.
# Lists, dictionaries and sets are mutable: they can change.
# Opening and closing times should normally stay unchanged.
# Nesting keeps connected information in one place.
# Too much nesting makes the code harder to read.
# Assignment shares a list; copy() makes a separate outer list.
# Later, loops could make displaying every session easier.
