# Store course details and students

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


course.students.append(Student("Abel", 80))
print(course.name)
print(course.teacher.name)
for student in course.students:
    print(student.name)
