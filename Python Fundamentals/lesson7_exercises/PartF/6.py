# Add and count students

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

    def student_count(self):
        return len(self.students)


teacher = Teacher("Ada")
course = Course("Python", teacher)


course.add_student(Student("Abel", 80))
print("Number of students:", course.student_count())
