def repeating_type(weekly_meal_plan):
    for i in range(len(weekly_meal_plan) - 1):
        if weekly_meal_plan[i]["type"] == weekly_meal_plan[i + 1]["type"]:
            return False
    return True


def using_up_food(weekly_meal_plan, food_inventory):
    skip = False
    for i in range(len(weekly_meal_plan) - 1):  # jenom weekly_meal_plan bez range?
        if skip:
            skip = False
            continue
        for key in weekly_meal_plan[i]["ingredients"]:
            if key < 1 and key in food_inventory["uzeniny"]:  # nejen uzeniny - opravit
                i += 1
                skip = True
                return True


def weekday_cooktime(weekly_meal_plan):
    if weekly_meal_plan[0:4]["cooktime"] <= 30:
        return


def add_specific_recipe(weekly_meal_plan):
    specific_recipe = input("What recipe would you like to include in this week's meal plan? ")
    specific_recipe = specific_recipe.lower()
    specific_day = input("Do you want to choose a specific day for this recipe? ")
    specific_day = specific_day.lower()

    while True:
        if specific_day != "no":
            if specific_recipe in weekly_meal_plan[specific_day]:
                break
        elif specific_day == "no":
            if specific_recipe in weekly_meal_plan:
                break
        else:
            print("Zkuste to znovu")
    return
