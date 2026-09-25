# Part 2 - Read the schedule

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

print("First title:", sessions[0]["title"])
print("Third speaker:", sessions[2]["speaker"])
print("Last room:", sessions[-1]["room"])
print("Second session:", sessions[1])
print("First start time:", sessions[0]["start"])
print("First three:", sessions[:3])
print("Last two:", sessions[-2:])

reversed_schedule = sessions[::-1]
part_of_schedule = sessions[2:5]
print("Reversed:", reversed_schedule)
print("Part of schedule:", part_of_schedule)
