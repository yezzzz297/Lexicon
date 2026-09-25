# Part 3 - Add product prices

def calculate_subtotal(*prices):
    total = 0
    for price in prices:
        total += price
    return total


print(calculate_subtotal(25))
print(calculate_subtotal(25, 50, 10))
print(calculate_subtotal())
