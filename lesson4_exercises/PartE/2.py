
def subtotal(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


def discount(amount, percent):
    return amount * (percent / 100)


def final_total(items, percent):
    sub_total = subtotal(items)
    discount_amount = discount(sub_total, percent)
    return sub_total - discount_amount


items = [
    {"price": 10, "quantity": 2},
    {"price": 25, "quantity": 1},
]

print(final_total(items, 10))
