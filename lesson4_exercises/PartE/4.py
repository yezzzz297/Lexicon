
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"


def farewell(name):
    """Return a goodbye message."""
    return f"Goodbye, {name}!"


if __name__ == "__main__":
    first_message = greet("Ada")
    second_message = farewell("Anna")
    print(first_message)
    print(second_message)
