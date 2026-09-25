# Use a shared pass score

class Student:
    # The pass score is shared by all students, so it is a class attribute.
    pass_score = 70

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        # A score of 70 or more is a pass.
        if self.score >= self.pass_score:
            return "PASS"
        else:
            return "FAIL"


student = Student("Abel", 80)
print("Pass score:", Student.pass_score)
print(student.name, student.get_status())
