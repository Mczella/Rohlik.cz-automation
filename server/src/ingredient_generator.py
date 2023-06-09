from math import ceil


def get_ingredients(weekly_meal_plan):
    ingredient_list = {}
    for recipe in weekly_meal_plan:
        for ingredient, value in recipe["ingredients"].items():
            if ingredient in ingredient_list:
                amount = ingredient_list[ingredient]
                amount += value
                ingredient_list[ingredient] = amount
            else:
                ingredient_list[ingredient] = value

    for ingredient, value in ingredient_list.items():
        ingredient_list[ingredient] = ceil(value)

    return ingredient_list
