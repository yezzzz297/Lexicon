class Booking:
    def __init__(self, customer, room, date, start_hour, end_hour):
        self.customer = customer
        self.room = room
        self.date = date
        self.start_hour = start_hour
        self.end_hour = end_hour

    def __str__(self):
        return f"{self.customer.name} booked {self.room.name} on {self.date} from {self.start_hour}:00 to {self.end_hour}:00"
