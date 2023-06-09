import requests


def get_favorites(authorization_cookie):
    response = requests.get(
        url="https://www.rohlik.cz/api/v1/categories/favorite/products",
        headers={"cookie": authorization_cookie},
        params={
            "page": 0,
            "size": 1000,
            #zvysit na 1000
        },
    )
    return response.json()


def get_product(product_id, authorization_cookie):
    response = requests.get(
        url="https://www.rohlik.cz/api/v1/products/{}".format(product_id),
        headers={
            "cookie": authorization_cookie,
        },
    )
    return response.json()


def get_product_price(product_id, authorization_cookie):
    response = requests.get(
        url="https://www.rohlik.cz/api/v1/products/{}/prices".format(product_id),
        headers={
            "cookie": authorization_cookie,
        },
    )
    return response.json()


def get_product_nutrition(product_id, authorization_cookie):
    response = requests.get(
        url="https://www.rohlik.cz/api/v1/products/{}/composition".format(product_id),
        headers={
            "cookie": authorization_cookie,
        },
    )
    if response.status_code != 404:
        return response.json()


def get_cart(authorization_cookie):
    response = requests.get(
        url="https://www.rohlik.cz/services/frontend-service/v2/cart",
        headers={"cookie": authorization_cookie},
    )
    return response.json()