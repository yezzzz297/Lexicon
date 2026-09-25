# Part 4 - Optional settings

def order_settings(**settings):
    result = {}
    for key, value in settings.items():
        if value is not None:
            result[key] = value
    return result


print(order_settings(shipping="express", discount=10))
print(order_settings(shipping="standard", gift=None))
