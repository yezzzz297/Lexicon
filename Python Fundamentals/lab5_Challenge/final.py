# Final challenge - Daily report from processed orders

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


def create_report(title, *sections, **metadata):
    # *sections handles different lengths instead of fixed section1/section2 fields.
    return {"title": title, "sections": list(sections), "metadata": metadata}


def format_report(report):
    # One normal parameter is clear; *args would hide what this function expects.
    text = report["title"] + "\n"
    for section in report["sections"]:
        text += section + "\n"
    for key, value in report["metadata"].items():
        text += f"{key}: {value}\n"
    return text


book = {"name": "Book", "price": 25}
mouse = {"name": "Mouse", "price": 50}

orders = [
    process_order(1, "Anna", book),
    process_order(2, "David", book, mouse),
    process_order(3, "Sara", mouse, discount=10),
    process_order(4, "Leo", book, shipping="express"),
    process_order(5, "Mia", book, gift_message="Happy birthday!")
]

totals = []
discounts = 0
express_orders = 0
for order in orders:
    totals.append(order["total"])
    discounts += order["discount"]
    if order["shipping"] == "express":
        express_orders += 1

report = create_report(
    "Daily Order Report",
    f"Orders: {len(orders)}",
    f"Revenue: {sum(totals)}",
    f"Average: {sum(totals) / len(totals)}",
    f"Largest order value: {max(totals)}",
    f"Smallest order value: {min(totals)}",
    f"Discounts: {discounts}",
    f"Express orders: {express_orders}",
    generated_by="Anna", department="Sales"
)
print(format_report(report))
