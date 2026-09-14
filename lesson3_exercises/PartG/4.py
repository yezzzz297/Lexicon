#Longest session without max()

sessions = [
    {"subject": "Python", "minutes": 60},
    {"subject": "AI", "minutes": 45},
    {"subject": "SQL", "minutes": 30},
    {"subject": "Python", "minutes": 50},
    {"subject": "Machine Learning", "minutes": 70},
    {"subject": "AI", "minutes": 40},
    {"subject": "SQL", "minutes": 55},
    {"subject": "Python", "minutes": 80},
    {"subject": "AI", "minutes": 65},
    {"subject": "Machine Learning", "minutes": 90}
]

longest = sessions[0]

for session in sessions:
    if session["minutes"] > longest["minutes"]:
        longest = session

print("Longest session:")
print(longest)