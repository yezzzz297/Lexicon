
value = 10

def change_value_wrong():
    value = value + 5
    print("Inside function:", value)

print("Original value:", value)

def return_new_value():

    return value + 5

print("New value from the function:", return_new_value())
print("Global value stays the same:", value)

