import sqlite3
from pathlib import Path


def connect():
    # Open the database beside this Python file.
    database_file = Path(__file__).parent / "webshop.db"
    conn = sqlite3.connect(database_file)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def list_products(conn):
    cursor = conn.execute("SELECT product_id, name, price, stock FROM products")
    for pid, name, price, stock in cursor.fetchall():
        print(f"{pid:>3}  {name:<20} {price:>8.2f} kr  ({stock} in stock)")


def search_customers(conn):
    city = input("City: ")
    cursor = conn.execute(
        "SELECT first_name, last_name FROM customers WHERE city = ?", (city,))
    rows = cursor.fetchall()
    if not rows:
        print("No customers found.")
    for first, last in rows:
        print(first, last)


def add_product(conn):
    name = input("Name: ")
    category = input("Category: ")
    # Exercise 7: abc causes a ValueError because it is not a number.
    try:
        price = float(input("Price: "))
    except ValueError:
        print("Please enter a number for the price.")
        return
    stock = int(input("Stock: "))
    conn.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (name, category, price, stock))
    conn.commit()
    print("Saved!")


# Exercise 5: change the stock of a product.
def change_stock(conn):
    product_id = int(input("Product id: "))
    new_stock = int(input("New stock: "))
    conn.execute(
        "UPDATE products SET stock = ? WHERE product_id = ?",
        (new_stock, product_id))
    conn.commit()
    print("Stock update saved!")


# Exercise 6: show an order's receipt with product names.
def show_receipt(conn):
    order_id = int(input("Order id: "))
    cursor = conn.execute("""
        SELECT products.name, order_items.quantity, order_items.unit_price
        FROM order_items
        JOIN products ON order_items.product_id = products.product_id
        WHERE order_items.order_id = ?
    """, (order_id,))
    rows = cursor.fetchall()
    if not rows:
        print("No items found for this order.")
        return
    total = 0
    for name, quantity, price in rows:
        line_total = quantity * price
        total = total + line_total
        print(f"{name}: {quantity} x {price:.2f} kr = {line_total:.2f} kr")
    print(f"Total: {total:.2f} kr")


# Exercise 8: show the three products with the most units sold.
def top_products(conn):
    cursor = conn.execute("""
        SELECT products.name, SUM(order_items.quantity) AS total_sold
        FROM products
        JOIN order_items ON products.product_id = order_items.product_id
        GROUP BY products.product_id, products.name
        ORDER BY total_sold DESC, products.product_id
        LIMIT 3
    """)
    rows = cursor.fetchall()
    for name, total_sold in rows:
        print(f"{name}: {total_sold} sold")


def main():
    conn = connect()
    while True:
        print("\n1) List products  2) Search customers  3) Add product  4) Change stock  5) Show receipt  6) Top 3 best-selling products  0) Quit")
        choice = input("> ")
        if choice == "1":
            list_products(conn)
        elif choice == "2":
            search_customers(conn)
        elif choice == "3":
            add_product(conn)
        elif choice == "4":
            change_stock(conn)
        elif choice == "5":
            show_receipt(conn)
        elif choice == "6":
            top_products(conn)
        elif choice == "0":
            break
    conn.close()


if __name__ == "__main__":
    main()
