from get import get_favorites, get_product, get_product_price, get_product_nutrition
import json
from login import login

authorization_cookie = login()
inventory = {}


# ONLY RUN ONCE
def fill_inventory():
    for product_id in get_favorites(authorization_cookie)["productIds"]:
        if get_product_nutrition(product_id, authorization_cookie) is not None:
            nutritional_values = get_product_nutrition(product_id, authorization_cookie)["nutritionalValues"]
        name = get_product(product_id, authorization_cookie)["name"]
        unit = get_product(product_id, authorization_cookie)["unit"]
        id_product = get_product(product_id, authorization_cookie)["id"]
        if get_product(product_id, authorization_cookie)["unit"] == "ks":
            textual_amount = int(get_product(product_id, authorization_cookie)["textualAmount"].split()[0])
        else:
            textual_amount = get_product(product_id, authorization_cookie)["textualAmount"]

        if get_product_price(product_id, authorization_cookie)["sales"] != []:
            price = get_product_price(product_id, authorization_cookie)["sales"][0]["price"]["amount"]

        else:
            price = get_product_price(product_id, authorization_cookie)["price"]["amount"]

        inventory[name] = {"product id": id_product, "unit": unit, "amount": textual_amount, "price": price, "nutritional values": nutritional_values}

    save_file = open("food_inventory.json", "w")
    json.dump(inventory, save_file, indent=4, ensure_ascii=False)
    save_file.close()


fill_inventory()
