# Print a course summary

class Student:
    def __init__(self, name, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100.")
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


course.add_student(Student("Abel", 90))
course.add_student(Student("Sara", 65))
course.add_student(Student("Alex", 70))
course.add_student(Student("Maya", 85))
course.add_student(Student("John", 45))


print("Course:", course.name)
print("Teacher:", course.teacher.name)
print("Number of students:", course.student_count())
print("Students who passed:")
for student in course.passed_students():
    print(student.name)
