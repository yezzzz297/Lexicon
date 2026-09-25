# Give each course a separate student list

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


other_course = Course("Math", teacher)
course.add_student(Student("Abel", 90))
print(course.name, course.student_count())
print(other_course.name, other_course.student_count())
