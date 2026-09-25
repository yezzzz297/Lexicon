# Start a course manager

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


teacher = Teacher("Aladdin")
course = Course("Python", teacher)


student = Student("Abel", 80)
course.students.append(student)
print(course.name, course.teacher.name, student.name)
