# Store a student name and score

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


student = Student("Abel", 80)
print(student.name, student.score)
