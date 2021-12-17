from objects import Product, Inventory

print('testing environment for fleamarkt')

book_1 = Product('Six Easy Pieces', 10.5, 'Bob', 1, 'books')
book_2 = Product('Ghandi', 8.1, 'Mark', 2, 'books')
book_3 = Product('Chess for Dummies', 1.0, 'Grad', 1, 'books')
camera_1 = Product('Canon', 80, 'Puma', 1, 'agd')
camera_2 = Product('Sony', 20, 'Lech', 3, 'agd')
notes_1 = Product('Notes from MIS', 11, 'Eva', 1,'notes')
notes_2 = Product('Thoughts from ISM', 2, 'Zaki', 1, 'notes')

# print(book_1)

inventory = Inventory()
# print(inventory)
inventory.add_product(book_1)
inventory.add_product(book_2)
inventory.add_product(book_3)
inventory.add_product(camera_1)
inventory.add_product(camera_2)
inventory.add_product(notes_1)
inventory.add_product(notes_2)

inventory.show_inventory()

inventory.del_product('Sony')

inventory.show_inventory()

food_1 = Product('Apple', 1, 'Hab', 3, 'food')
food_2 = Product('Orange', 2, 'Malik', 1, 'food')

inventory.add_product(food_1)
inventory.add_product(food_2)

inventory.show_inventory()
