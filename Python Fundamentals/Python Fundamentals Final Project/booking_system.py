class BookingSystem:
    def __init__(self):
        self.bookings = []

    def add_booking(self, booking):
        if booking in self.bookings:
            print("This booking is already in the system. Create a new booking instead.")
            return

        if booking.start_hour < 0 or booking.start_hour > 23:
            print("Start hour must be between 0 and 23.")
        elif booking.end_hour < 1 or booking.end_hour > 24:
            print("End hour must be between 1 and 24.")
        elif booking.end_hour <= booking.start_hour:
            print("End hour must be later than start hour.")
        else:
            for existing_booking in self.bookings:
                if existing_booking.status == "Confirmed":
                    if booking.room == existing_booking.room and booking.date == existing_booking.date:
                        if booking.start_hour < existing_booking.end_hour and booking.end_hour > existing_booking.start_hour:
                            print("This room is already booked during that time.")
                            return

            booking.status = "Confirmed"
            self.bookings.append(booking)
            print("Booking added.")
            print(f"Total cost: {booking.calculate_cost()} SEK")

    def cancel_booking(self, booking):
        if booking in self.bookings:
            if booking.status == "Cancelled":
                print("This booking is already cancelled.")
            else:
                booking.status = "Cancelled"
                print("Booking cancelled.")
        else:
            print("Booking not found.")

    def show_bookings(self):
        if len(self.bookings) == 0:
            print("No bookings yet.")
        else:
            for booking in self.bookings:
                print(booking)
