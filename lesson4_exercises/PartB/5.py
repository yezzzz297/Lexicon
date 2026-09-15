
def calculate_discount(price, percent):
    """Return the price after applying a percentage discount."""
    discount_amount = price * (percent / 100)
    return price - discount_amount


print(calculate_discount(100, 10))
print(calculate_discount(80, 25))
