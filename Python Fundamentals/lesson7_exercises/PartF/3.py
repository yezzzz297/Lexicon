# Check a student status

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        # A score of 70 or more is a pass.
        if self.score >= 70:
            return "PASS"
        else:
            return "FAIL"


student = Student("Abel", 80)
print(student.get_status())
