
def outer_function():
    message = "Hello from the outer function"

    def inner_function():
        print("Inner function sees:", message)

    inner_function()
    print("Outer function still has:", message)


outer_function()
