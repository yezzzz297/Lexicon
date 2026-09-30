from room import Room
from customer import Customer
from booking import Booking
from booking_system import BookingSystem


room = Room("Grace", 6)
customer = Customer("Ada", "ada@example.com")
system = BookingSystem()

print("Meeting Room Booking System")
print(room)
print(customer)

date = "2026-10-01"
print(f"Booking date: {date}")

while True:
    print("\n1. Add booking")
    print("2. View bookings")
    print("3. Cancel booking")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        start_hour = input("Start hour (0-23): ")
        end_hour = input("End hour (1-24): ")

        if start_hour.isdecimal() and end_hour.isdecimal():
            start_hour = int(start_hour)
            end_hour = int(end_hour)
            booking = Booking(customer, room, date, start_hour, end_hour)
            system.add_booking(booking)
        else:
            print("Please enter whole hours using digits, such as 10 and 12.")

    elif choice == "2":
        system.show_bookings()

    elif choice == "3":
        if len(system.bookings) == 0:
            print("No bookings to cancel.")
        else:
            number = 1
            for booking in system.bookings:
                print(f"{number}. {booking}")
                number = number + 1

            booking_number = input("Enter the booking number to cancel: ")

            if booking_number.isdecimal():
                booking_number = int(booking_number)
                if booking_number >= 1 and booking_number <= len(system.bookings):
                    booking = system.bookings[booking_number - 1]
                    system.cancel_booking(booking)
                else:
                    print("Booking number not found.")
            else:
                print("Please enter a booking number using digits.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Please choose 1, 2, 3, or 4.")
