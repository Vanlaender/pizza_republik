# objects used by fleamarkt

import itertools
import datetime
from enum import Enum


class Action(Enum):
    SELL = 1
    BUY = 2


class Product:
    id_iteration = itertools.count()

    def __init__(self, name: str, action: Action, price: float, amount: int = 1, category: str = 'no_subject'):
        self.id = next(Product.id_iteration)
        self.name = name
        self.action = action
        self.price = price
        self.category = category
        self.amount = amount
        self.date = datetime.datetime.now()

    def get_action(self):
        return self.action

    def get_json(self):
        return [{
            "id": self.id,
            "name": self.name,
            "action": self.action,
            "price": self.price,
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }]

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, action: {self.action}"


class Inventory:

    def __init__(self):
        self.to_sell = []
        self.to_buy = []
        self.load_inventory()

    def load_inventory(self):
        pass

    def save_inventory(self):
        pass

    def update_inventory(self):  # not sure if save or update it's not redundant
        pass

    def add_product(self, product: Product):
        if product.get_action() == Action.SELL:
            self.to_sell.append(product)
        elif product.get_action() == Action.BUY:
            self.to_buy.append(product)
        else:
            return -1

    def show_inventory(self):
        print('to sell')
        for sell in self.to_sell:
            print(sell)

        print('to buy')
        for buy in self.to_buy:
            print(buy)

    def __str__(self):
        return f"This is one and only inventory."
