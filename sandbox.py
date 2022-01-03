# differences:
# - bot is imported from the discord.ext.commands module
# - the bot initializer requires a command_prefix
#   command is an order that a user gives to a bot so that it will do sth.
#   commands are different from events because they are:
#       - arbitrarily defined
#       - directly called by the user
#       - flexible, in terms of their interface

import os
import random

# 1
import discord
from discord.ext import commands
from dotenv import load_dotenv

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


@bot.command(name='roll', aliases=['kosci', 'kostki'], help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int = 1, number_of_sides: int = 6):  # in the article it's called Converter, but is it?
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range (number_of_dice)
    ]
    await ctx.send(', '.join(dice))


@bot.command(name='create-channel')
@commands.has_role('admin')  # this is called a Check - might be useful
async def create_channel(ctx, channel_name='fritz'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.names, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)


@bot.event
async def on_command_error(ctx, error):  # this will print this error in Discord not on stdout
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')