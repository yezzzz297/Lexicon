# Validate a score with ValueError

class Student:
    def __init__(self, name, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100.")
        self.name = name
        self.score = score


student = Student("Abel", 80)
print(student.name, student.score)

# An invalid score raises ValueError.
try:
    student = Student("Alex", 120)
except ValueError as error:
    print(error)
