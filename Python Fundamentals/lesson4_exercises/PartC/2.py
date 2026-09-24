
def calculate_price(price, quantity=1, discount=0):
    total = price * quantity
    return total - discount


print(calculate_price(50))
print(calculate_price(50, 2))
print(calculate_price(50, 2, 10))
print(calculate_price(price=50, quantity=3, discount=5))
