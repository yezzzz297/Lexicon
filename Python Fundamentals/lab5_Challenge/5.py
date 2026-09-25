# Part 5 - Two examples of each kind of unpacking

def show_product(name, price):
    print(name, price)


def register_customer(name, email, customer_id):
    return {"name": name, "email": email, "id": customer_id}


book = ["Book", 25]
mouse = ("Mouse", 50)
show_product(*book)
show_product(*mouse)

anna = {"name": "Anna", "email": "anna@example.com", "customer_id": 1}
david = {"name": "David", "email": "david@example.com", "customer_id": 2}
print(register_customer(**anna))
print(register_customer(**david))

# * unpacks positional values; ** matches dictionary keys to parameter names.
