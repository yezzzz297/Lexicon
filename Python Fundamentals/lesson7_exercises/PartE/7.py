# Print the names of students in a course

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Teacher:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

teacher = Teacher("Mr. Aladdin")
course = Course("Python Fundamentals", teacher)

course.add_student(Student("Yetnayet", 90))
course.add_student(Student("Sara", 65))
course.add_student(Student("Ada", 70))

for student in course.students:
    print(student.name)
