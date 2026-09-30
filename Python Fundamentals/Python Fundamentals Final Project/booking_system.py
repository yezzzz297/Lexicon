class BookingSystem:
    def __init__(self):
        self.bookings = []

    def add_booking(self, booking):
        self.bookings.append(booking)
        print("Booking added.")

    def show_bookings(self):
        if len(self.bookings) == 0:
            print("No bookings yet.")
        else:
            for booking in self.bookings:
                print(booking)
