
def greet(name):
    return f"Hello, {name}!"


def farewell(name):
    return f"Goodbye, {name}!"


if __name__ == "__main__":
    first_message = greet("Ada")
    second_message = farewell("Anna")
    print(first_message)
    print(second_message)
