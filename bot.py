import discord, datetime, asyncio
from typing import Optional
from discord import app_commands
from discord.ext import commands, tasks
from secrets import randbelow

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents = intents)

# Task to make Kiriko Bot send a random voice line to a random channel
@tasks.loop()
async def randomly_send_voiceline():

    # A variety of Kiriko's voicelines
    voicelines = ["Carried on the wind", "Let me balance you out", "Like a gentle rain", "The breeze brings relief", 
                  "Ho ho hey", "Huh, lonely in here", "Aw, I feel all warm inside", "What's up?", "I could use a heal",
                  "I take care of my friends", "I've got a few tricks", "Wait 'til you see me on my bike", 
                  "I'm obviously the most precious", "Scry some more!", "You can still be good... while being up to no good",
                  "Lure me out... I dare you", "Just don't get caught"]

    # bot-commands, overwatch, fartnite
    channels = [1214641001059192853, 1215366792277524590, 1214626990548717569]

    # Randomly generate which voiceline and channel to use
    random_voiceline = randbelow(len(voicelines))
    random_channel = randbelow(len(channels))

    # Set how many seconds until the task is executed again
    randomly_send_voiceline.change_interval(seconds = randbelow(28801))

    channel = client.get_channel(channels[random_channel])
    await channel.send(voicelines[random_voiceline])

# Sync the tree commands
@client.event
async def on_ready():
    print(f'You have logged in as {client.user}')
    print("Ready!")

    # Wait a random amount of seconds until we send the first voiceline
    await asyncio.sleep(randbelow(28801))
    await randomly_send_voiceline.start()

# This needs the bot's token, which only Hunter has
client.run('')