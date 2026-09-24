
def count_signs(numbers):
    """Return counts for positive, negative, and zero values."""
    result = {"positive": 0, "negative": 0, "zero": 0}
    for number in numbers:
        if number > 0:
            result["positive"] += 1
        elif number < 0:
            result["negative"] += 1
        else:
            result["zero"] += 1
    return result


print(count_signs([3, -2, 0, 4, 0, -1]))
