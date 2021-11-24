# bot.py

import os
import random
from dotenv import load_dotenv

# differences:
# - bot is imported from the discord.ext.commands module
# - the bot initializer requires a command_prefix
#   command is an order that a user gives to a bot so that it will do sth.
#   commands are different from events because they are:
#       - arbitrarily defined
#       - directly called by the user
#       - flexible, in terms of their interface

# 1
from discord.ext import commands

load_dotenv()
WIKIBOTIA_TOKEN = os.getenv('WIKIBOTIA_TOKEN')

# 2
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='the_office', help='Gives a random TWSS joke from The Office')
async def the_office(ctx):
    # ctx = context
    quotes = [
        "Can You Make That Straighter?",
        "You're Hardly My First!",
        "You Always Left Me Satisfied & Smiling",
        "And You Were Directly Under Her The Entire Time?",
        "Michael, I Can’t Believe You Came"
    ]

    response = random.choice(quotes)
    await ctx.send(response)

bot.run(WIKIBOTIA_TOKEN)

