# Fleamarkt - marketplace bot for discord community

import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
FLEAMARKT_TOKEN = os.getenv('FLEAMARKT_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


bot.run(FLEAMARKT_TOKEN)