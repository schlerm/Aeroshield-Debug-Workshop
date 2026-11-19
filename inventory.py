def reserve_inventory(products, order):
    products_by_id = {product["id"]: product for product in products}
    requested = {}

    for item in order["items"]:
        product_id = item["product_id"]
        quantity = item["quantity"]
        if product_id not in products_by_id or type(quantity) is not int or quantity <= 0:
            return False
        requested[product_id] = requested.get(product_id, 0) + quantity

    if any(products_by_id[product_id]["stock"] < quantity for product_id, quantity in requested.items()):
        return False

    for product_id, quantity in requested.items():
        products_by_id[product_id]["stock"] -= quantity

    return True


def restock_product(products, product_id, amount):
    for product in products:
        if product["id"] == product_id:
            product["stock"] = amount
            return product
    return None
