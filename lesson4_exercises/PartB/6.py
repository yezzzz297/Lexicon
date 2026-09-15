
def add_and_print(a, b):
    """Print the result but do not return it."""
    print(a + b)


def add_and_return(a, b):
    """Return the result so it can be used later."""
    return a + b


print("Example with print:")
value1 = add_and_print(3, 4)
print("value1:", value1)

print("\nExample with return:")
value2 = add_and_return(3, 4)
print("value2:", value2)

