
def get_total(numbers):
    """Add all numbers in the list."""
    total = 0
    for number in numbers:
        total += number
    return total


def get_average(numbers):
    """Return the average value of the numbers."""
    if not numbers:
        return 0
    return get_total(numbers) / len(numbers)


def print_summary(numbers):
    """Show the total and average clearly."""
    print(f"Total: {get_total(numbers)}")
    print(f"Average: {get_average(numbers)}")


print_summary([10, 20, 30, 40])
