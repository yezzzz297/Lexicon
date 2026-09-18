
students = [
    {"name": "David", "score": 78},
    {"name": "Sarah", "score": 49},
    {"name": "Isac", "score": 88},
    {"name": "Mike", "score": 55},
]

result = {student["name"]: ("PASS" if student["score"] >= 50 else "FAIL") for student in students}
print(result)
