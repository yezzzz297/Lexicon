
students = [
    {"name": "Ada", "score": 78},
    {"name": "Adam", "score": 92},
    {"name": "Sarah", "score": 64},
    {"name": "Isac", "score": 88},
]

ascending = sorted(students, key=lambda student: student["score"])
descending = sorted(students, key=lambda student: student["score"], reverse=True)

print("Ascending:", ascending)
print("Descending:", descending)
