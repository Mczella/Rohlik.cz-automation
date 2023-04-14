def get_product_id(food_inventory, ingredient):
    for product in food_inventory:
        if ingredient == product:
            return food_inventory[product]["nutritional values"][0]["productId"]
            #returns productId of the ingredient to add the product to cart