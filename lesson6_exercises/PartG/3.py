
students = [
    {"name": "Abel", "score": 72},
    {"name": "Ada", "score": 55},
    {"name": "Sarah", "score": 48},
    {"name": "Mike", "score": 80},
]

passing_students = [
    {"name": student["name"], "score": student["score"]}
    for student in students
    if student["score"] >= 60
]
print(passing_students)
