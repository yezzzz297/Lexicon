# A parent cannot use a method defined only in its child

class Employee:
    def __init__(self, name):
        self.name = name

    def get_information(self):
        return "Employee: " + self.name


class Developer(Employee):
    def write_code(self):
        return self.name + " is writing code."


employee = Employee("Grace")
# write_code belongs to Developer, not Employee.
try:
    print(employee.write_code())
except AttributeError:
    print("An Employee does not have a write_code method.")
