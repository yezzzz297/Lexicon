# Update a score with validation

class Student:
    def __init__(self, name, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100.")
        self.name = name
        self.score = score

    def get_status(self):
        # Use 70 as the pass score for these exercises.
        if self.score >= 70:
            return "PASS"
        else:
            return "FAIL"

    def update_score(self, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100.")
        self.score = score

student = Student("Sara", 65)
print(student.name, student.score, student.get_status())
student.update_score(80)
print(student.name, student.score, student.get_status())
try:
    student.update_score(105)
except ValueError as error:
    print(error)
print("Score after rejected update:", student.score)
