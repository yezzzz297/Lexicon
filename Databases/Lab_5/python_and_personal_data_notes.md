Lab 5: Python and personal data

My files

Exercises 1 to 3 are in python_exercises.py. Exercises 5 to 8 are in shop.py, which is based on the teacher's original file. Exercises 9 to 11 are in Lab_5_Exercises_9-11.sql. The written answers are below. The programs use the webshop.db database.

How to run the Python exercises

Close the database in DB Browser first. Open the terminal in VS Code from the Class_Exercise folder. To run exercises 1 to 3, enter this command:

python3 Databases/Lab_5/python_exercises.py

The program shows the customers, asks for a maximum price, and asks for a category. Enter Shoes, Clothing, or Accessories with a capital letter.

To run the shop program, enter this command:

python3 Databases/Lab_5/shop.py

Choose option 4 to change stock, option 5 to see an order's receipt, or option 6 to see the three products with the most units ordered. Choose 0 to quit. Adding a product or changing stock saves the change in the database. The top three results include items from cancelled orders.

How to run the SQL exercises

Open webshop.db from the Databases/Lab_5 folder in DB Browser. Run exercises 9 to 11 one at a time in Execute SQL. For exercise 11, create the view once, then run the SELECT statement below it to see the customers.

When finished, click Revert Changes as the worksheet asks. This undoes the database changes. The saved SQL file still contains the answers.

Exercise 4

An f-string puts the user's input directly into the SQL command. Someone could type SQL code that changes what the command does. A question mark placeholder keeps the input separate, so SQLite treats it as a value instead of SQL code.

Exercise 7

If the user types abc as the price, Python cannot change it into a number. This causes a ValueError and stops the original program. I used try and except to show a message and return to the menu without adding a product.

Exercise 12

I would ask why the shop needs a birth date, because just in case is not a clear reason to collect it. If the shop does not need it, I would leave it out to avoid collecting extra personal information.
