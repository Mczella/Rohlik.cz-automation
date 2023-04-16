from create_fzf import create_recipe
import json
from json.decoder import JSONDecodeError
import os

recipe = create_recipe()


def add_recipe(recipe):
    if not os.path.exists("json_recipes.json") or os.path.getsize("json_recipes.json") == 0:
        json_recipes = []
    else:
        with open('json_recipes.json', 'r') as data:
            try:
                json_recipes = json.load(data)
            except JSONDecodeError as n:
                print(n)
                print("Recipes file is not valid.")
                return
    json_recipes.append(recipe)
    save_file = open("json_recipes.json", "w")
    json.dump(json_recipes, save_file, indent=4, ensure_ascii=False)
    save_file.close()

print(recipe)

add_recipe(recipe)