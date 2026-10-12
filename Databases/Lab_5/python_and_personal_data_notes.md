# Lab 5: Python and personal data

## My files

- `python_exercises.py`: exercises 1–3.
- `shop.py`: exercises 5–8, added to the code given.
- `Lab_5_Exercises_9-11.sql`: exercises 9–11.
- This file: answers to exercises 4 and 12, and an explanation of exercise 7.
- `webshop.db`: the database used by the programs.

## How to run the Python files

Close the database in DB Browser first. In the VS Code terminal, start from
the `Class_Exercise` folder and run:

```sh
python3 Databases/Lab_5/python_exercises.py
```

This shows the customers, asks for a maximum price, and then asks for a
category. For the category, type `Shoes`, `Clothing`, or `Accessories` with
a capital letter.

To open the shop menu, run:

```sh
python3 Databases/Lab_5/shop.py
```

- Option 4 changes how many items of a product are in stock.
- Option 5 shows the products and total price for an order.
- Option 6 shows the three products with the most units ordered.
- Option 0 closes the program.

Adding a product or changing stock saves the change in `webshop.db`.
The top-three query counts all order items, including cancelled orders.


## Exercise 4

Using an f-string puts the user's input straight into the SQL command.
Someone could type SQL code and change what the command does.
Using `?` keeps the input separate, so SQLite reads it as a value, not as
part of the SQL command.

## Exercise 7

If the user types `abc` as the price, Python cannot turn it into a number.
This causes a `ValueError`, and the original program stops.
I used `try/except` to show a message and return to the menu instead.
No product is added when the price is invalid.

## Exercise 12

I would ask why the shop needs a birth date, because “just in case” is not
a clear reason to collect it. If the shop does not need it, I would leave
it out to avoid collecting extra personal information.

