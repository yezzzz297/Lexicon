# Print each student status

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

student1 = Student("Yetnayet", 90)
student2 = Student("Sara", 65)
student3 = Student("Alex", 70)
student4 = Student("Maya", 85)
student5 = Student("John", 45)
student6 = Student("Lina", 78)

students = [student1, student2, student3, student4, student5, student6]

for student in students:
    print(student.name, student.get_status())
