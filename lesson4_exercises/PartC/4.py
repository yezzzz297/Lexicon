
def create_order(product, quantity, price):
    """Return an order dictionary."""
    return {
        "product": product,
        "quantity": quantity,
        "price": price,
    }


print(create_order(price=35, product="Notebook", quantity=2))
