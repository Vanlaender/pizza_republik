# Objects used by fleamarkt bot.

import itertools


class Product:
    id_iteration = itertools.count()

    def __init__(self, name: str, price: float, owner: int, category: str = 'no_subject', currency: str = 'CHF'):
        self.id = next(Product.id_iteration)
        self.name = name
        self.price = price
        self.owner = owner
        self.category = category
        self.currency = currency

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, price: {self.price}, owner: {self.owner}"


class Inventory:

    def __init__(self):
        self.for_sale = []

    def add_product(self, product: Product):
        self.for_sale.append(product)

    def del_product(self, idd: int):
        for product in self.for_sale:
            if product.id == idd:
                self.for_sale.remove(product)
                break

    def last_n_products(self, n: int):
        if n <= 0:
            return []
        else:
            return self.for_sale[-n:]

    def __str__(self):
        return f"This will be Fleamarkt inventory."
