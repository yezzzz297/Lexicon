from room import Room
from customer import Customer
from booking import Booking
from booking_system import BookingSystem


rooms = [Room("Grace", 6), Room("Ocean", 10), Room("Forest", 4)]
system = BookingSystem()

print("Meeting Room Booking System")

date = "2026-10-01"
print(f"Booking date: {date}")

while True:
    print("\n1. Add booking")
    print("2. View bookings")
    print("3. Cancel booking")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        valid_name = False
        while valid_name == False:
            name = input("Customer name: ")
            for character in name:
                if character != " " and character != "\t":
                    valid_name = True

            if valid_name == False:
                print("Name cannot be empty or only spaces.")

        email = input("Customer email: ")
        # This is a basic check, not a full email address check.
        while "@" not in email or "." not in email or " " in email:
            print("Email must contain @ and a dot, with no spaces.")
            email = input("Customer email: ")

        customer = Customer(name, email)

        print("Choose a room:")
        number = 1
        for room in rooms:
            print(f"{number}. {room}")
            number = number + 1

        valid_room = False
        while valid_room == False:
            room_number = input("Choose a room number: ")
            if room_number.isdecimal():
                room_number = int(room_number)
                if room_number >= 1 and room_number <= len(rooms):
                    room = rooms[room_number - 1]
                    valid_room = True
                else:
                    print("Room number not found.")
            else:
                print("Please enter a room number using digits.")

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
