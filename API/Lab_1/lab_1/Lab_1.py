from urllib.parse import quote

import requests

# Task 3: get_json is kept in its own file.
from api_client import get_json

BASE = "https://fakestoreapi.com"


# Task 1: Sort products by price
print("\nTask 1: Sort products by price")
products = get_json(f"{BASE}/products")

if products is not None:
    products = sorted(products, key=lambda product: product["price"])
    for product in products:
        print(f"{product['price']:.2f} - {product['title']}")


# Task 2: Look at the categories
print("\nTask 2: Look at the categories")
categories = get_json(f"{BASE}/products/categories")

if categories is not None:
    print(categories)
    category = input("Choose a category: ").strip().lower()

    if category not in categories:
        print("That category does not exist.")
    else:
        category_path = quote(category, safe="")
        url = f"{BASE}/products/category/{category_path}"
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
url = f"{BASE}/products"
new_product = {
    "title": "Student backpack",
    "price": 29.99,
    "description": "A backpack for school.",
    "image": "https://example.com/backpack.jpg",
    "category": "men's clothing",
}

# Create a product.
try:
    response = requests.post(url, json=new_product, timeout=5)
    print("POST status:", response.status_code)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException as error:
    print(f"Could not create the product: {type(error).__name__}")

# Change the price of product 7.
changes = {"price": 19.99}
try:
    response = requests.patch(f"{url}/7", json=changes, timeout=5)
    print("PATCH status:", response.status_code)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException as error:
    print(f"Could not update the price: {type(error).__name__}")

print("This fake API does not save the changes.")


# Task 5: Test error handling
print("\nTask 5: Test error handling")
print("1. Wrong URL:")
get_json(f"{BASE}/this-endpoint-does-not-exist")

print("\n2. Very short timeout:")
get_json(f"{BASE}/products", timeout=0.001)

print("\n3. Made-up domain:")
get_json("https://made-up-api.invalid/products")

print("\nAll three attempts finished without crashing.")
