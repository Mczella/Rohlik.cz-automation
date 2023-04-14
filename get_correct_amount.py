def get_correct_amount(food_inventory, product, amount):
    if food_inventory[product]["unit"] == "ks":
        amount = amount / food_inventory[product]["textualAmount"]
    return amount
