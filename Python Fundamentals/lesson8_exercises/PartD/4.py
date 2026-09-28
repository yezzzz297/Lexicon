# Use inherited methods

class Employee:
    def __init__(self, name):
        self.name = name

    def get_information(self):
        return "Employee: " + self.name


class Developer(Employee):
    def write_code(self):
        return self.name + " is writing code."


class Manager(Employee):
    def hold_meeting(self):
        return self.name + " is holding a meeting."


developer = Developer("Ada")
manager = Manager("Sara")
print(developer.get_information())
print(manager.get_information())
