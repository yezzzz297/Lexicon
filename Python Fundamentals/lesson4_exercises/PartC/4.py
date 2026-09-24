
def create_order(product, quantity, price):
    return {
        "product": product,
        "quantity": quantity,
        "price": price,
    }


print(create_order(price=35, product="Notebook", quantity=2))
