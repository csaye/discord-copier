import discord
import asyncio
from threading import Thread
from time import sleep

tokenfile = open('./token.txt')
TOKEN = tokenfile.read()
tokenfile.close()

# Use discord.Client() instead of bot
client = discord.Client()


# Start a Thread for the bot to just loop forever
def init():
    loop = asyncio.get_event_loop()
    loop.create_task(client.start(TOKEN))
    Thread(target=loop.run_forever).start()


# Once the bot is ready, have it loop forever and write a message to
# the main channel
@client.event
async def on_ready():
    print("Discord bot logged in as: %s, %s" % (client.user.name, client.user.id))
    general = None

    #TODO: There has to be a better way to do this
    # Get a referance to the general channel
    for c in client.get_all_channels():
        if c.name == "general":
            general = c
    
    while True:
        await general.send("Test message")
        sleep(5)
        


init()
# Show the main thread is still going
while True:
    print("This is the main thread")
    sleep(7)