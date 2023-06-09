from get import get_favorites, get_product, get_product_price, get_product_nutrition
import json
from login import login

authorization_cookie = login()


def update_inventory():
    with open('food_inventory.json', 'r') as food_inventory:
        data = json.load(food_inventory)
    for product_id in get_favorites(authorization_cookie)["productIds"]:
        # adds new favorite products
        if get_product(product_id, authorization_cookie)["name"] not in data:
            name = get_product(product_id, authorization_cookie)["name"]
            if get_product_nutrition(product_id, authorization_cookie) is not None:
                nutritional_values = get_product_nutrition(product_id, authorization_cookie)["nutritionalValues"]

            if get_product_price(product_id, authorization_cookie)["sales"] != []:
                price = get_product_price(product_id, authorization_cookie)["sales"][0]["price"]["amount"]

            else:
                price = get_product_price(product_id, authorization_cookie)["price"]["amount"]
            data[name] = {"price": price, "nutritional values": nutritional_values}

        # updates prices
        name = get_product(product_id, authorization_cookie)["name"]
        id = get_product(product_id, authorization_cookie)["id"]
        data[name]["product_id"] = id
        if get_product_price(product_id, authorization_cookie)["sales"] != []:
            if get_product_price(product_id, authorization_cookie)["sales"][0]["price"]["amount"] != data[name]["price"]:
                new_price = get_product_price(product_id, authorization_cookie)["sales"][0]["price"]["amount"]
                data[name]["price"] = new_price
        else:
            if get_product_price(product_id, authorization_cookie)["price"]["amount"] != data[name]["price"]:
                new_price = get_product_price(product_id, authorization_cookie)["price"]["amount"]
                data[name]["price"] = new_price

    save_file = open("food_inventory.json", "w")
    json.dump(data, save_file, indent=4, ensure_ascii=False)
    save_file.close()

update_inventory()