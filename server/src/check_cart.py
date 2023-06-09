from food_keys import get_product_id
import json

with open("food_inventory.json", "r") as file:
    food_inventory = json.load(file)


def check_cart(shopping_list, cart):
    buy_elsewhere = {}
    for key, value in shopping_list.items():
        key_id = get_product_id(food_inventory, key)
        if str(key_id) not in cart["data"]["items"]:
            buy_elsewhere[key] = value
        for k in cart["data"]["items"]:
            if str(key_id) == k and value > cart["data"]["items"][k]["quantity"]:
                new_amount = value - cart["data"]["items"][k]["quantity"]
                buy_elsewhere[key] = new_amount

    return buy_elsewhere

