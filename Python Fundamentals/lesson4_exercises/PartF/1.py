
def min_max(values):
    if not values:
        return None, None

    smallest = values[0]
    largest = values[0]

    for value in values[1:]:
        if value < smallest:
            smallest = value
        if value > largest:
            largest = value

    return smallest, largest


print(min_max([5, 2, 9, 1, 7]))
