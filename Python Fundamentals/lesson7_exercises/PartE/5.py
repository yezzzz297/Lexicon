# Give a course an empty student list

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

teacher = Teacher("MR. Aladdin")
course = Course("Python Fundamentals", teacher)

print("Students:", course.students)
