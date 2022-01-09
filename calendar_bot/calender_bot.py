import discord # discord
from discord.ext import tasks # needed to utilize mindless task of checking reminders
import datetime # needed to utilize the datetime objects and such
import os


client = discord.Client()
global Events #global variable that can be accessed by the other functions -- stores the events
Events = [] # Events is being assigned an empty list which will be filled when events are added
CALENDER_TOKEN = os.getenv('CALENDER_TOKEN')


@tasks.loop(seconds=10) #The amount of time the loop will slumber, until its time do its task
async def check_events(): #Name is irrelevant
    current_date = datetime.date.today() # Collects a datetime of the current date storing it to variable of current_date
    print(current_date.strftime("%d-%b-%Y")) # Prints the message in the console for verifcation purposes, it will be formated
    channel = client.get_channel(929040126103928913) # grabs textcahnnel object utilizing the id of the calender bot text chat
    for event in Events: #iterates over the events
        date = datetime.datetime(int(event[1][2]), int(event[1][1]), int(event[1][0])) # Creates date time from stored event
        date_formatted = date.strftime("%d-%b-%Y") # formats the  datetime event so its clean in message
        print(date_formatted) # print for verfication in console
        if date.isocalendar() == current_date.isocalendar(): #checks to see if the tuple of isocalender matches, if so it be same day
            await channel.send("Reminder:: " + event[0] + " on " + date_formatted + " is happening today!!!") # send message about it being same day
            Events.pop() #removes the event as it doesnt need to be reminded and it will be over by the next day
        elif date.isocalendar()[1] == current_date.isocalendar()[1] and date.year == current_date.year: #checks to see if the week number and year are same
            await channel.send("Reminder:: " + event[0] + " on " + date_formatted + " is happening this week!!!") #if it is same, send message event happens this week



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) # shows messge if it connects with name and such
    check_events.start() # starts the infinite loop of tasks, forever turning and checking time


@client.event
async def on_message(message):
    if message.author == client.user: # Just ignores any messages from the bot
        return # it works :)))))))))))))))))))))))))))))))))))))))))

    if message.content.startswith('!addevent'):         # How it reacts to addevent
        event_name = message.content.split(":")[0][10:] # Splits the message into half, creating the event with what ever follow !addevent
        date = message.content.split(":")[1] # Reverse of thing above, retrieves dat from last half of input message
        date_format = date.split(".") # Splits the date retrieved into list containing the DD/MM/YYYY
        print(date_format) # Prints message in console for verificaiton
        event = [event_name, date_format] # creating an "Event" that will be stored in the global events list
        Events.append(event) # Appends it to the last position
        print(Events) # Prints all the events in console for verifcaiton

    if message.content.startswith("!rmevent"): # How it reacts to rmevent aka remove event
        event_to_remove = message.content[9:] # Retrieves event name off what ever follows !rmevent
        print(event_to_remove) # print the name of event to be removed in console for verfication
        for event in Events: # Loop to iterate over all events in the Events list
            print(event[0]) # Print the name of the current event
            if event[0] == event_to_remove: # If the name of the intended deleted event is the same
                Events.pop() # Removes the event from the list

    if message.content.startswith("!viewevents"): #How bot reacts to viewevents, name implies the function
        for event in Events: # iterate over all events
            date_format = datetime.datetime(int(event[1][2]), int(event[1][1]), int(event[1][0])) # Create a date time object utilizing the input data stored in the Event
            await message.channel.send("Event: " + event[0] + " Date:" + date_format.strftime("%d-%b-%Y")) # Sends message with the datetime object formated to day-month(short) year

client.run(CALENDER_TOKEN)

