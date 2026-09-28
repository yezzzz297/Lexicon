# Add a manager method

class Employee:
    def __init__(self, name):
        self.name = name

    def get_information(self):
        return "Employee: " + self.name


class Manager(Employee):
    def hold_meeting(self):
        return self.name + " is holding a meeting."


manager = Manager("Sara")
print(manager.hold_meeting())
