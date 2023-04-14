from pyfzf.pyfzf import FzfPrompt
from food_keys import get_food_keys
from get_correct_amount import get_correct_amount

import json

with open('food_inventory.json', 'r') as data:
    food_inventory = json.load(data)

def create_recipe():
    fzf = FzfPrompt()
    recipe = {}
    ingredient = {}
    q1 = input("Add recipe name. ")
    q2 = input("Add recipe type. ")
    q3 = input("Add cook time. ")
    q4 = input("Do you want to choose an ingredient? y/n ")
    recipe["name"] = q1
    recipe["type"] = q2
    recipe["cook time"] = q3
    # recipe["ingredients"] = q4

    while True:
        choice = fzf.prompt(get_food_keys())
        #'--multi')
        amount = fzf.prompt(range(0,30))
        if food_inventory[choice[0]]["unit"] == "ks":
            amount[0] = float(amount[0]) / food_inventory[choice[0]]["amount"]
        # get_correct_amount(food_inventory, choice, amount)
        ingredient[choice[0]] = float(amount[0])
        recipe["ingredients"] = ingredient
        q5 = input("Do you want to add another ingredient? y/n ")
        if q5 == "n":
            break
    return recipe


# print(create_recipe())



# def add_recipe(recipe):
#     with open('json_recipes.json', 'r') as data:
#         json_recipes = json.load(data)
#     json_recipes.update(recipe)
#     save_file = open("json_recipes.json", "w")
#     json.dump(data, save_file, indent=4, ensure_ascii=False)
#     save_file.close()
#
#
# add_recipe(recipe)