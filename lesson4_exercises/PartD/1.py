
def calculate_total(numbers):
    """Add all numbers in a list and return the total."""
    total = 0
    for number in numbers:
        total += number
    return total


print(calculate_total([1, 2, 3, 4, 5]))
