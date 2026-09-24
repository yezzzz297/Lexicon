
def average(*numbers):
    if not numbers:
        return 0

    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


print(average(10, 20, 30))
print(average())
