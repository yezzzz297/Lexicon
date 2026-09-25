# Find students who passed

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        # A score of 70 or more is a pass.
        if self.score >= 70:
            return "PASS"
        else:
            return "FAIL"


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

    def passed_students(self):
        passed = []
        for student in self.students:
            if student.get_status() == "PASS":
                passed.append(student)
        return passed


teacher = Teacher("Ada")
course = Course("Python", teacher)


course.add_student(Student("Abel", 80))
course.add_student(Student("Alex", 50))
for student in course.passed_students():
    print(student.name)
