import discord # Discord

client = discord.Client()
global password # Create global variable
password = None # Assign it as null to start with


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))  # shows messge if it connects with name and such


@client.event
async def on_message(message):

    if message.channel.id == 926787840464019496: #Channel id of the motd text channel
        await message.delete() # deletes ever message posted in motd
    global password #accessess global variable

    if message.content.startswith('!pc'): # !pc, for changing password, anything that follows !pc is password
        roles = message.author.roles # retrieves the roles of the user
        for role in roles: #iterates over the collected roles
            if role.name == "@admin": # if user is admin they are allowed to change password
                password = hash(message.content[3:]) #one way hash the password so its not stored in plain text, assigned to global variable password

    if password == None: # if password is none prints this message when its receives message
        print("Exception Handling :)")

    if message.content.startswith('!ps'): # for changing the passowrd
        if message.author == client.user: # ignores if its the bots message for some reason
            return
        role = discord.utils.get(message.guild.roles, name="Verified") #retrieves the verified role object
        member = message.author # retrieves the member object of the message author
        if hash(message.content[3:]) == password: #one way hash the input password, if it same as global it same as password
            await member.add_roles(role) # gives user the verified role, allowing them to views all the other channels
            channel = client.get_channel(910494238876270604) # gets channel object for text channel general
            await channel.send("Welcome " + str(message.author) + " to the server!!!") # Prints welcome message that contains the name of the user who just got verified

client.run('')


