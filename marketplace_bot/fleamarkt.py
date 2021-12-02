# Fleamarkt - marketplace bot for discord community

import os

from discord.ext import commands
from dotenv import load_dotenv
from objects import Product, Inventory, Action

load_dotenv()
FLEAMARKT_TOKEN = os.getenv('FLEAMARKT_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='hi')
async def hi(ctx):
    await ctx.send('Hello')


six_easy = Product('six easy pieces', Action.SELL, 10.5, 1, 'books')
ghandi = Product('Ghandi', Action.SELL, 8.1, 2, 'books')
camera = Product('Canon', Action.SELL, 80, 1, 'agd')

print(six_easy)
print(ghandi)
# del six_easy

bottle = Product('Dopper', Action.SELL, 100, 1)  # it looks like id will be going up and up (no reuse)
print(bottle)
print(bottle.get_json())

inventory = Inventory()
print(inventory)
print(bottle.get_action())
inventory.add_product(six_easy)
inventory.add_product(camera)

inventory.show_inventory()

# bot.run(FLEAMARKT_TOKEN)