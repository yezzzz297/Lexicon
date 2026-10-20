from urllib.parse import quote

import requests

# Task 3: get_json is kept in its own file.
from api_client import get_json


# Task 1: Sort products by price
print("\nTask 1: Sort products by price")
products = get_json("https://fakestoreapi.com/products")

if products is not None:
    products = sorted(products, key=lambda product: product["price"])
    for product in products:
        print(f"{product['price']:.2f} - {product['title']}")


# Task 2: Look at the categories
print("\nTask 2: Look at the categories")
categories = get_json("https://fakestoreapi.com/products/categories")

if categories is not None:
    print(categories)
    category = input("Choose a category: ").strip().lower()

    if category not in categories:
        print("That category does not exist.")
    else:
        url = "https://fakestoreapi.com/products/category/" + quote(category, safe="")
        products = get_json(url)

        if products is not None:
            print("Number of products:", len(products))
            if products:
                cheapest = min(products, key=lambda product: product["price"])
                print("Cheapest:", cheapest["title"], "-", cheapest["price"])
            else:
                print("No products in this category.")


# Task 4: Create and change a product
print("\nTask 4: Create and change a product")
url = "https://fakestoreapi.com/products"
product = {
    "title": "Student backpack",
    "price": 29.99,
    "description": "A backpack for school.",
    "image": "https://example.com/backpack.jpg",
    "category": "men's clothing",
}

# Create a product.
try:
    response = requests.post(url, json=product, timeout=10)
    print("POST status:", response.status_code)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException:
    print("Could not create the product. Check your connection or try again.")

# Change the price of product 7.
try:
    response = requests.patch(url + "/7", json={"price": 19.99}, timeout=10)
    print("PATCH status:", response.status_code)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException:
    print("Could not update the price. Check your connection or try again.")

print("This fake API does not save the changes.")
