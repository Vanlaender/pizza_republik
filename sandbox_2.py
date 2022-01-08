# sandbox_2.py
# This bot checks some term in wikipedia and returns short note & url about inquiry

import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
WIKIBOTIA_TOKEN = os.getenv('WIKIBOTIA_TOKEN')
GUILD = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    # this for loop can be replaced with discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    # or with discord.utils.get(client.guilds, name=GUILD)
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} has connected to Discord!')
    print(f'{guild.name}(id: {guild.id})')

    # members = '\n - '.join([member.name for member in guild.members])
    # print(f'Guild members:\n - {members}')
    # this is not working as I expected: only Wikibotia is on the list


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@client.event
async def on_message(message):
    # client can't tell the difference between a bot user and a normal user
    # protection from recursive case
    if message.author == client.user:
        return

    quotes = [
        'Nie weszles',
        'Damian nie strzelaj',
        'Jestem diabel wcielony',
        'Rob salto kiemon'
    ]

    if message.content == 'polska gurom':
        response = random.choice(quotes)
        await message.channel.send(response)
    # error handling
    # elif message.content == 'raise-exception':
    #     raise discord.DiscordException

    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday!')


# error handling
# if the exception originated in the on_message() event handler, you write() to the file err.log
@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


client.run(WIKIBOTIA_TOKEN)

# there are two ways in discord.py to implement an event handler:
# 1. using the client.event decorator
# 2. creating a subclass of Client and overriding its handler methods
# take a look at how to subclass Client:

# class CustomClient(discord.Client):
#     async def on_ready(self):
#         print(f'{self.user} has connected to Discord!')
#
#
# client = CustomClient()
# client.run(WIKIBOTIA_TOKEN)
