import json
from math import ceil


with open('food_inventory.json', 'r') as data:
    food_inventory = json.load(data)

with open("json_recipes.json", 'r') as file:
    recipes = json.load(file)


def add_price(food_inventory, recipes):
    for product in recipes:
        price = 0
        for ingredient in product["ingredients"]:
            price += food_inventory[ingredient]["price"]
        print(product["portion"])
        product["price"] = ceil(price)
        product["price per portion"] = ceil(price / product["portion"])

    save_file = open("json_recipes.json", "w")
    json.dump(recipes, save_file, indent=4, ensure_ascii=False)
    save_file.close()

add_price(food_inventory, recipes)
