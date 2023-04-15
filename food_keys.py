import json


with open('food_inventory.json', 'r') as data:
    food_inventory = json.load(data)


def get_food_keys():
    food_list = []
    for key in food_inventory.keys():
        food_list.append(key)

    return food_list


def get_product_id(food_inventory, ingredient):
    for product in food_inventory:
        if ingredient == product:
            return food_inventory[product]["nutritional values"][0]["productId"]
            #returns productId of the ingredient to add the product to cart
