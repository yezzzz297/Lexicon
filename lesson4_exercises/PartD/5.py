
def average_score(students):
    """Return the average score of all students."""
    if not students:
        return 0

    total = 0
    for student in students:
        total += student["score"]

    return total / len(students)


students = [
    {"name": "Ana", "score": 90},
    {"name": "Ben", "score": 80},
    {"name": "Cleo", "score": 70},
]

print(average_score(students))
