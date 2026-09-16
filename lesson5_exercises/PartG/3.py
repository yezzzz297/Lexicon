
def stats(numbers):
    if not numbers:
        return {
            "count": 0,
            "total": 0,
            "average": 0,
            "min": None,
            "max": None,
        }

    count = 0
    total = 0
    current_min = numbers[0]
    current_max = numbers[0]

    for num in numbers:
        count += 1
        total += num
        if num < current_min:
            current_min = num
        if num > current_max:
            current_max = num

    average = total / count
    return {
        "count": count,
        "total": total,
        "average": average,
        "min": current_min,
        "max": current_max,
    }


print(stats([4, 7, 9, 2, 5]))
print(stats([]))
