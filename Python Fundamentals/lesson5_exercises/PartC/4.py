
# The asterisk in a function definition means the function accepts extra values.


def sum_three(a, b, c):
    return a + b + c


numbers = [10, 20, 30]
print(sum_three(*numbers))
# args unpack and add`three (10,20,30)
# The * in the function call expands the list into separate values.
# The * in the function definition is different: it collects extra arguments.
