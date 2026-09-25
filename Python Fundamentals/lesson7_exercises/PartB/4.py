# Complete and reopen a task

class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def complete(self):
        self.completed = True

    def reopen(self):
        self.completed = False

task = Task("Study Python")
task.complete()
print("Completed:", task.completed)
task.reopen()
print("After reopening:", task.completed)
