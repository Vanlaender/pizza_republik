# wikibotia.py
# This bot checks some term in wikipedia and returns short note & url about inquiry

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('WIKIBOTIA_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run(TOKEN)
