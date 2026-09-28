# Add a developer method

class Employee:
    def __init__(self, name):
        self.name = name

    def get_information(self):
        return "Employee: " + self.name


class Developer(Employee):
    def write_code(self):
        return self.name + " is writing code."


developer = Developer("Ada")
print(developer.write_code())
