# Create an employee

class Employee:
    def __init__(self, name):
        self.name = name

    def get_information(self):
        return "Employee: " + self.name


employee = Employee("Grace")
print(employee.get_information())
