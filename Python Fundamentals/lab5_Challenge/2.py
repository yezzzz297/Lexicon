# Part 2 - Create five different orders

def create_order(order_id, customer, *products, **details):
    # *products allows any number instead of fixed product1/product2 parameters.
    # **details is easier than defining a parameter for every possible note.
    return {"id": order_id, "customer": customer,
            "products": list(products), "details": details}


orders = [
    create_order(1, "Anna", "Laptop"),
    create_order(2, "David", "Phone", "Mouse", shipping="express"),
    create_order(3, "Sara", "Book", "Notebook", discount=10),
    create_order(4, "Leo", "Chair", priority=True, gift_message="Enjoy!"),
    create_order(5, "Mia", "Desk", campaign="SUMMER26", delivery="Reception")
]

for order in orders:
    print(order)
