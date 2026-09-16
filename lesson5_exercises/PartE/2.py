

def calculate_order(customer, *prices, **options):
    subtotal = sum(prices)
    discount = options.get("discount", 0)
    shipping_fee = options.get("shipping_fee", 0)
    total = subtotal - discount + shipping_fee

    order = {
        "customer": customer,
        "prices": list(prices),
        "subtotal": subtotal,
        "discount": discount,
        "shipping_fee": shipping_fee,
        "total": total,
    }
    return order


print(calculate_order("Ada", 12, 18, 7, discount=5, shipping_fee=3))
