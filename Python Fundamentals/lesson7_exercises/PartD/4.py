# Return PASS or FAIL

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        # Use 70 as the pass score for these exercises.
        if self.score >= 70:
            return "PASS"
        else:
            return "FAIL"

student = Student("Yetnayet", 90)
print(student.name, student.get_status())
