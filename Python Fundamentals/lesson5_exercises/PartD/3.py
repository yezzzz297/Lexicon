
def build_product(name, price, **metadata):
    product = {"name": name, "price": price}
    product.update(metadata)
    return product

print(build_product("HandBag", 800, brand="YSL", color="black"))
