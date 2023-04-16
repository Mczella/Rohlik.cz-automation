from random import randint, sample
from food_keys import get_product_id
from login import login
from post import post_cart
from rules import repeating_type
import json
from ingredient_generator import get_ingredients
from get import get_cart
from check_cart import check_cart

with open("food_inventory.json", "r") as file:
    food_inventory = json.load(file)

with open("json_recipes.json", 'r') as file:
    recipes = json.load(file)

with open("regular_groceries.json", 'r') as file:
    groceries = json.load(file)

authorization_cookie = login()


def weekly_meal_generator():
    while True:
        weekly_meal_plan = sample(recipes, 7)
        if repeating_type(weekly_meal_plan):
        # add more rules
            break
    return weekly_meal_plan


weekly_meal_plan = (weekly_meal_generator())
meal_plan = []  #to create new file with planned recipes
for recipe in weekly_meal_plan:
    meal_plan.append(recipe["name"])
for ingredient, amount in get_ingredients(weekly_meal_plan).items():
    print(ingredient, amount)
shopping_list = get_ingredients(weekly_meal_plan)
print(shopping_list)
for product in groceries: #add groceries to shopping list
    if product in shopping_list:
        shopping_list[product] += groceries[product]
    else:
        shopping_list[product] = groceries[product]

print(shopping_list)


for ingredient in shopping_list:
    product_id = get_product_id(food_inventory, ingredient)
    amount = shopping_list[ingredient]
    post_cart(authorization_cookie, product_id, amount)

cart = get_cart(authorization_cookie)
buy_elsewhere = check_cart(shopping_list, cart)

save_file = open("buy_elsewhere.json", "w")
json.dump(buy_elsewhere, save_file, indent=4, ensure_ascii=False)
save_file.close()

save_file = open("meal_plan.json", "w")
json.dump(meal_plan, save_file, indent=4, ensure_ascii=False)
save_file.close()
