from room import Room
from customer import Customer
from booking import Booking


room = Room("Ocean", 6)
print(room)

customer = Customer("Ada", "ada@example.com")
print(customer)

# Times use whole hours on a 24-hour clock.
booking = Booking(customer, room, "2026-10-01", 10, 12)
print(booking)
