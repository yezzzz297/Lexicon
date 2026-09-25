# Store students in a list

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

students = [student1, student2, student3, student4, student5, student6]

print("Number of students:", len(students))
