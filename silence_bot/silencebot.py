import discord # Discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) # shows messge if it connects with name and such

@client.event
async def on_message(message):
    if message.author == client.user: #Checks if message is bot
        return #ignores message if bot

    if message.content.startswith('!JC_Stop'): # how bot handles if they want to unmute someone
        roles = message.author.roles # gathers the roles of the message person
        channel = message.author.voice.channel # gets the channel where the individual is connected to
        for role in roles: #iterates over the role of the author
            if role.name == "Presenter": # if they have presenter role, they are authorized to utilize command
                await message.channel.send("Isn't it time to end the tyranny? For everyone?") # Sends message signaling people are unmuted
                current_members = channel.members #grabs all the current members of the channel connected
                for member in current_members: # iterates over all the members connected
                    await member.edit(mute=False) # mutes all the users in the voice channel


    if message.content.startswith('!JC_Help'): # how bot react if person wants to mute non-presenters
        roles = message.author.roles # gathers roles of the sender
        channel = message.author.voice.channel # gets the voice channel that the person is currently connected to
        for role in roles: #iterate over the roles
            if role.name == "Presenter": # if they have presenter role they are allowed to utilize this
                await message.channel.send("Let's try some word association. First word: " + str(channel)) # mesage signaling people are getting muted
                current_members = channel.members # grabs the currentley connected members in the voice channel
                for member in current_members: # iterates over the members
                    roles_of_user = member.roles # grabs the roles of the members
                    for role in roles_of_user: # iterates over all the roles
                        if role.name == "Attendee": # if they have attendee role they can continue
                            await member.edit(mute=True) # mutes the user if they are attendee

client.run('')


