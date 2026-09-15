
def find_student(students, name):
    """Find a student record by name. Return None if not found."""
    for student in students:
        if student["name"] == name:
            return student
    return None


students = [
    {"name": "Ada", "grade": 90},
    {"name": "Anna", "grade": 85},
]

print(find_student(students, "Ada"))
print(find_student(students, "Anna"))
