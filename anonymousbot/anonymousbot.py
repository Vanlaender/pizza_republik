import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!pm'):
        server = client.get_guild(910494238335197185)
        anon = message.author
        member = await server.fetch_member(anon.id)
        print(member)
        if anon == member:
            channel = client.get_channel(927617333214740541)
            await channel.send(message.content[3:])

client.run('')


