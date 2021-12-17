# objects used by fleamarkt

import itertools
import datetime
from enum import Enum


class Product:
    id_iteration = itertools.count()

    def __init__(self, name: str, price: float, owner: str, amount: int = 1, category: str = 'no_subject'):
        self.id = next(Product.id_iteration)
        self.name = name
        self.price = price
        self.owner = owner  # later maybe this should be discord id type
        self.category = category
        self.amount = amount
        self.date = datetime.datetime.now()

    def get_json(self):
        return [{
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "owner": self.owner,
            "amount": self.amount,
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

    def del_product(self, name: str = None):
        for product in self.for_sale:
            if product.name == name:
                self.for_sale.remove(product)
                print('item sold')
                break

    def show_inventory(self):
        print('Items for sale: ')
        for sell in self.for_sale:
            print(sell)

    def __str__(self):
        return f"This is my inventory"
