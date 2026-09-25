# Find students above a score threshold

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

    def students_above(self, threshold):
        result = []
        for student in self.students:
            if student.score > threshold:
                result.append(student)
        return result


teacher = Teacher("Ada")
course = Course("Python", teacher)


course.add_student(Student("Abel", 90))
course.add_student(Student("Alex", 60))
for student in course.students_above(80):
    print(student.name, student.score)
