# objects used by fleamarkt

import itertools
import datetime
from enum import Enum


class Product:
    id_iteration = itertools.count()

    def __init__(self, name: str, price: float, owner: int, category: str = 'no_subject'):
        self.id = next(Product.id_iteration)
        self.name = name
        self.price = price
        self.owner = owner  # later maybe this should be discord id type
        self.category = category
        self.date = datetime.datetime.now()

    def get_json(self):
        return [{
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "owner": self.owner,
            "category": self.category,
            "date": self.date
        }]

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, price: {self.price}, owner: {self.owner}"


class Inventory:

    def __init__(self):
        self.for_sale = []
        self.load_inventory()

    # later - load from file
    def load_inventory(self):
        pass

    # later - save to file
    def save_inventory(self):
        pass

    def add_product(self, product: Product):
        self.for_sale.append(product)

    def del_product(self, id: int):
        for product in self.for_sale:
            if product.id == id:
                self.for_sale.remove(product)
                print('item sold:', product)
                break

    def show_inventory(self):
        print('Items for sale: ')
        for sell in self.for_sale:
            print(sell)

    def last_n_products(self, n: int):
        if n <= 0:
            return []
        else:
            return self.for_sale[-n:]

    def __str__(self):
        return f"This is Fleamarkt inventory."
