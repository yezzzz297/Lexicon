# Meeting Room Booking System

This is a simple Python project for booking meeting rooms.

## What the program does

- You enter your name and email.
- You choose a room, date, start hour, and end hour.
- Each room has a price per hour. The program calculates the total cost.
- You can view bookings and see their status.
- You can cancel a booking by choosing its number from the list.
- Cancelled bookings stay in the list, but the room becomes free for that time.
- The program checks dates and hours. It also stops two confirmed bookings from using the same room at the same time.

For example, Grace costs 100 SEK per hour. A booking from 10 to 12 costs 200 SEK.

## How to run
After running the code.

Choose a number from the menu:

1. Add booking
2. View bookings
3. Cancel booking
4. Exit

Enter dates like `2026-11-01`. Use whole hours, such as `8` and `12`.
The start hour can be 0 to 23. The end hour can be 1 to 24 and must be later than the start hour.

## Files

- room.py: Stores the room name, capacity, and hourly price.
- customer.py: Stores the customer name and email.
- booking.py: Stores booking details, keeps the status, and calculates the cost.
- booking_system.py: Adds, shows, and cancels bookings. It checks for time conflicts.
- date_check.py: Checks if a date is valid, including leap years.
- main.py: Shows the menu and asks the user for input.

## Things to know

Bookings are only saved while the program is running.
Cancelled bookings still show their original cost. The program does not take payments.
The email check is simple and does not check if the email account exists.
