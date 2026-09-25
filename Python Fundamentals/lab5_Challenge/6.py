# Part 6 - Flexible order summary

def order_summary(order_id, customer, *notes, **details):
    text = f"Order: {order_id}\nCustomer: {customer}\n"
    for note in notes:
        text += note + "\n"
    for key, value in details.items():
        text += f"{key}: {value}\n"
    return text


print(order_summary(1, "Anna", "Pack carefully", "Leave at reception", priority=True))
print(order_summary(2, "David"))
