# Change one object without changing another

class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def complete(self):
        self.completed = True

    def reopen(self):
        self.completed = False

task1 = Task("Study Python")
task2 = Task("Read a book")
task1.complete()
print(task1.title, task1.completed)
print(task2.title, task2.completed)
