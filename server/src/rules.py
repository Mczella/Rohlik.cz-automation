def repeating_type(weekly_meal_plan):
    for i in range(len(weekly_meal_plan) - 1):
        if weekly_meal_plan[i]["type"] == weekly_meal_plan[i + 1]["type"]:
            return False
    return True
