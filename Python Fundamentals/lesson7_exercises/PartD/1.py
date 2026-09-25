# Create six students

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

student1 = Student("Yetnayet", 90)
student2 = Student("Sara", 65)
student3 = Student("Alex", 70)
student4 = Student("Maya", 85)
student5 = Student("John", 45)
student6 = Student("Lina", 78)

print(student1.name, student2.name, student3.name, student4.name, student5.name, student6.name)
