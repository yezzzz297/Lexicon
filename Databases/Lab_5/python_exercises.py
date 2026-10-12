
# i use the database connection function from shop.py.
from shop import connect


# Exercise 1: show every customer.
def exercise_1(conn):
    cursor = conn.execute(
        "SELECT first_name, last_name, city FROM customers")
    rows = cursor.fetchall()
    for first, last, city in rows:
        print(f"{first} {last} ({city})")


# Exercise 2: show products below a chosen price.
def exercise_2(conn):
    try:
        max_price = float(input("Maximum price: "))
    except ValueError:
        print("Please enter a number.")
        return
    # ? keeps the user's value separate from the SQL code.
    cursor = conn.execute(
        "SELECT name, price FROM products WHERE price < ?",
        (max_price,))
    rows = cursor.fetchall()
    if not rows:
        print("No products found.")
    for name, price in rows:
        print(f"{name}: {price:.2f} kr")


# Exercise 3: count products in a category.
def exercise_3(conn):
    category = input("Category: ")
    cursor = conn.execute(
        "SELECT COUNT(*) FROM products WHERE category = ?",
        (category,))
    row = cursor.fetchone()
    number_of_products = row[0]
    print(f"Number of products: {number_of_products}")


conn = connect()

exercise_1(conn)
exercise_2(conn)
exercise_3(conn)

conn.close()
