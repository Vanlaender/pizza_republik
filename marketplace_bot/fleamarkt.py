# Fleamarkt - marketplace bot for discord community

import os

import discord
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


# tu zaczac
@bot.command(name='priv')
async def priv(ctx, user: discord.Member, *, message=None):  # this * takes multiple arguments and stacks them as one
    message = message or 'Siema byku'
    await user.send(message)


@bot.event
async def on_message(message):
    await bot.process_commands(message)  # without this the whole script is dying
    print(message)

inventory = Inventory()

bot.run(FLEAMARKT_TOKEN)
