
def calculate_discount(price, percent):
    discount_amount = price * (percent / 100)
    return price - discount_amount


print(calculate_discount(100, 10))
print(calculate_discount(80, 25))
