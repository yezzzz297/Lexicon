
students = [
    {"name": "Abel", "score": 90},
    {"name": "Ada", "score": 70},
    {"name": "Sarah", "score": 85},
]

def get_score(student):
    return student["score"]

normal_sort = sorted(students, key=get_score)
lambda_sort = sorted(students, key=lambda student: student["score"])

print("Normal function:", normal_sort)
print("Lambda:", lambda_sort)


