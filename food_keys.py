import json


with open('food_inventory.json', 'r') as data:
    food_inventory = json.load(data)

def get_food_keys():
    food_list = []
    for key in food_inventory.keys():
        food_list.append(key)

    return food_list


