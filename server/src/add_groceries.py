from create_fzf import create_groceries
import json
from json.decoder import JSONDecodeError
import os

groceries = create_groceries()


def add_groceries(groceries):
    if not os.path.exists("regular_groceries.json") or os.path.getsize("regular_groceries.json") == 0:
        regular_groceries = {}
    else:
        with open('regular_groceries.json', 'r') as data:
            try:
                regular_groceries = json.load(data)
            except JSONDecodeError:
                print("Groceries file is not valid.")
                return
    for product in groceries:
        regular_groceries[product] = groceries[product]
    save_file = open("regular_groceries.json", "w")
    json.dump(regular_groceries, save_file, indent=4, ensure_ascii=False)
    save_file.close()


print(groceries)

add_groceries(groceries)