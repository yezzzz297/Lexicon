# Part 9 - Reuse one function for different order types

def calculate_subtotal(*prices):
    return sum(prices)


def process_order(order_id, customer, *products, shipping="standard", discount=0, **details):
    prices = []
    for product in products:
        prices.append(product["price"])
    subtotal = calculate_subtotal(*prices)

    shipping_cost = 0
    if shipping == "express":
        shipping_cost = 15

    return {
        "id": order_id, "customer": customer, "products": list(products),
        "subtotal": subtotal, "discount": discount, "shipping": shipping,
        "shipping_cost": shipping_cost, "total": subtotal - discount + shipping_cost,
        "details": details
    }


book = {"name": "Book", "price": 25}
mouse = {"name": "Mouse", "price": 50}

orders = [
    process_order(1, "Anna", book),
    process_order(2, "David", book, mouse),
    process_order(3, "Sara", mouse, discount=10),
    process_order(4, "Leo", book, shipping="express"),
    process_order(5, "Mia", book, gift_message="Happy birthday!")
]

for order in orders:
    print(order)
