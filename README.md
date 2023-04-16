# Rohlik.cz automation

Generate weekly recipes and fill in your rohlik.cz cart with just 1 click.

## Requirements

* [Pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today)

## Setup

1. Copy `login.py.example` to `login.py` and fill in your Rohlik.cz credentials.
2. Install dependencies: 

```
pipenv install
```

# Run

First of all, fill your favorites food inventory by running (this is only done once):
```
pipenv run python fill_inventory.py
```
To later update products and prices, run:
```
pipenv run python update.py
```
To add recipe, run:
```
pipenv run python add_recipe.py
```
To add regular groceries, run:
```
pipenv run python add_groceries.py
```
And finally, to fill your cart with a week's worth of groceries, run:
```
pipenv run python init.py
```
This will fill your cart, generate `meal_plan.json` to see planned meals and `buy_elsewhere.json` to see groceries that were not available and must be bought elsewhere.

