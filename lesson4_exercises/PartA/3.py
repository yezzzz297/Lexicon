# Part A - Basic math functions
# These functions take numbers and return a result.


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract the second number from the first."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide two numbers. Avoid dividing by zero."""
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))
