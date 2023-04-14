def generate_shopping_list(weekly_meal_plan, food_inventory):
    shopping_list = {}
    # shipping_list[weekly_meal_plan[0]["ingredients"][0]] = weekly_meal_plan[0]["ingredients"][1]
    for key, value in weekly_meal_plan[0]["ingredients"].items():
        shipping_list[key] = value