from get import get_favorites, get_product, get_product_price, get_product_nutrition
import json
from login import login
import requests


def post_cart(authorization_cookie, product_id, amount):
    response = requests.post(
        url="https://www.rohlik.cz/services/frontend-service/v2/cart",
        headers={"content-type": "application/json", "cookie": authorization_cookie},
        data=json.dumps({"quantity":amount,
                         "productId":str(product_id),
                         "recipeId":None,
                         "actionId":None,
                         "source":
                             "true:Favorites"})
    )

