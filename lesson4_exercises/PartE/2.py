
def subtotal(items):
    """Add up the price of each item."""
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


def discount(amount, percent):
    """Calculate a discount value."""
    return amount * (percent / 100)


def final_total(items, percent):
    """Return the price after the discount is applied."""
    sub_total = subtotal(items)
    discount_amount = discount(sub_total, percent)
    return sub_total - discount_amount


items = [
    {"price": 10, "quantity": 2},
    {"price": 25, "quantity": 1},
]

print(final_total(items, 10))
