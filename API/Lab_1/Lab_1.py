from urllib.parse import quote

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
