# Use a teacher object in a course

class Teacher:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

teacher = Teacher("Mr. Aladdin")
course = Course("Python Fundamentals", teacher)

print(course.name, course.teacher.name)
