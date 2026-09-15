
def greet(name, greeting="Hello"):
    """Greet someone using a default  message."""
    print(f"{greeting}, {name}!")


greet("Ada")
greet("Ada", "Hi")
greet(name="Ada", greeting="Welcome")
