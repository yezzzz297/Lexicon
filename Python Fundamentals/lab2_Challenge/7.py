# Part 7 - Connect the separate lists

titles = ["Python", "Java", "AI Basics"]
speakers = ["Ada", "Grace", "Alan"]
rooms = ["A", "B", "C"]

sessions = [
    {"title": titles[0], "speaker": speakers[0], "room": rooms[0],
     "start": "09:00", "duration": 60, "topic": "AI"},
    {"title": titles[1], "speaker": speakers[1], "room": rooms[1],
     "start": "10:00", "duration": 45, "topic": "Web"},
    {"title": titles[2], "speaker": speakers[2], "room": rooms[2],
     "start": "11:00", "duration": 60, "topic": "AI"}
]

print(sessions[1]["title"])
print(sessions[1]["speaker"])
print(sessions[1]["room"])

