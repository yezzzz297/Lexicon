class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return f"{self.name} (capacity: {self.capacity})"
