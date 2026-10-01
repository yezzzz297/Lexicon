class Room:
    def __init__(self, name, capacity, price_per_hour):
        self.name = name
        self.capacity = capacity
        self.price_per_hour = price_per_hour

    def __str__(self):
        return f"{self.name} (capacity: {self.capacity}, price: {self.price_per_hour} SEK per hour)"
