
from api_client import get_json

products = get_json("https://fakestoreapi.com/products")

if products is not None:
    products = sorted(products, key=lambda product: product["price"])
    for product in products:
        print(f"{product['price']:.2f} - {product['title']}")
