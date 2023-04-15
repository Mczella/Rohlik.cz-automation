from random import randint, sample
from get import get_favorites, get_product, get_product_price, get_product_nutrition
from get_amount import get_amount
from food_keys import get_product_id
from login import login
from post import post_cart
from rules import repeating_type, using_up_food, weekday_cooktime, add_specific_recipe
import yaml
import requests
import json
from ingredient_generator import get_ingredients
from get import get_cart
from check_cart import check_cart

with open("food_inventory.json", "r") as file:
    food_inventory = json.load(file)

# with open("recipes.yml", 'r') as file:
#     recipes = yaml.safe_load(file)
# authorization_cookie = login()

with open("json_recipes.json", 'r') as file:
    recipes = json.load(file)
authorization_cookie = login()


def weekly_meal_generator():
    while True:
        weekly_meal_plan = sample(recipes, 1)
        if repeating_type(weekly_meal_plan):
        # and weekday_cooktime(weekly_meal_plan) \
        # and using_up_food(weekly_meal_plan, food_inventory) \
        #     and add_specific_recipe(weekly_meal_plan):
        # add more rules
            break
    return weekly_meal_plan


weekly_meal_plan = (weekly_meal_generator())
for recipe in weekly_meal_plan:
    print(recipe)
for ingredient, amount in get_ingredients(weekly_meal_plan).items():
    print(ingredient, amount)
ingredient_list = get_ingredients(weekly_meal_plan)

for ingredient in ingredient_list:
    product_id = get_product_id(food_inventory, ingredient)
    amount = (get_amount(ingredient, ingredient_list))
    post_cart(authorization_cookie, product_id, amount)

cart = get_cart(authorization_cookie)
buy_elsewhere = check_cart(ingredient_list, cart)

save_file = open("buy_elsewhere.json", "w")
json.dump(buy_elsewhere, save_file, indent=4, ensure_ascii=False)
save_file.close()

