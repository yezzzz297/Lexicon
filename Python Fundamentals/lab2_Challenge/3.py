# Part 3 - Change the schedule

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

participants = ["Anna", "David", "Sara", "Leo", "Mia", "Noah", "Nora", "Oscar", "Lina", "Yusuf"]

print("Before:", sessions)
print("Participants before:", participants)

sessions[0]["room"] = "C"
sessions[0]["capacity"] = 25
sessions[1]["speaker"] = "Abel"
sessions[0]["difficulty"] = "Beginner"

new_session = {"title": "Python Help", "speaker": "Ada", "room": "A",
               "start": "15:00", "duration": 30, "topic": "Python", "capacity": 40}
sessions.append(new_session)
cancelled = sessions.pop(3)
participants.append("Ruth")
participants.remove("Yusuf")

print("After:", sessions)
print("Cancelled:", cancelled["title"])
print("Participants after:", participants)
