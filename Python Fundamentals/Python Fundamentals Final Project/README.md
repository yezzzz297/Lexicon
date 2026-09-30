# Meeting Room Booking System

A Python terminal program for booking meeting rooms.

## Features

- Enter a customer name and email, and choose a room.
- Choose a date in YYYY-MM-DD format and whole hours on a 24-hour clock.
- View and cancel bookings using the menu.
- Reject invalid dates, invalid hours, and overlapping bookings for the same room and date.
- Cancel a booking to make its time available again.

## How to run

Open a terminal in this project folder and run:

```sh
python3 main.py
```

Use menu options 1 to 4. No extra packages are needed.

## Files

- `room.py`: Room name and capacity.
- `customer.py`: Customer name and email.
- `booking.py`: Connects a customer, room, date, and hours.
- `booking_system.py`: Stores, checks, displays, and cancels bookings.
- `date_check.py`: Checks calendar dates, including leap years.
- `main.py`: Runs the menu and reads user input.

Bookings exist only while the program runs. Dates may be in the past or future.
Each booking starts and ends on the same date; 24 is allowed as the end hour.
Email validation is a basic format check, not verification of an email account.
