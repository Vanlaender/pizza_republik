import discord
import os

client = discord.Client()
ANONYMOUS_TOKEN = os.getenv('ANONYMOUS_TOKEN')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!pm'):
        member = message.author
        channel = client.get_channel(927617333214740541)
        await channel.send(message.content[3:])

client.run(ANONYMOUS_TOKEN)


