# Part 1 - Conference data

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

print("Speakers:", speakers)
print("Rooms:", rooms)
print("Participants:", participants)
print("Topics:", topics)
print("Hours:", hours)
print("Sessions:", sessions)

# Lists keep items in order. Each dictionary describes one session.
# A set keeps unique topics. A tuple holds the opening and closing times.
