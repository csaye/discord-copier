import time, threading, asyncio
from discord.ext import commands

# read token from file
tokenfile = open('./token.txt')
token = tokenfile.read()
tokenfile.close()

bot = commands.Bot(command_prefix='!')
context = None
last_timestamp = None

# checks for message to send
async def check_message():
    global last_timestamp, context
    # read message from file
    f = open('./message.txt')
    text = f.read()
    if not text: return
    timestamp, message = text.splitlines()
    f.close()
    # if new message, send to context
    if timestamp != last_timestamp and context:
        print(f'sending message {message}')
        last_timestamp = timestamp
        await context.send(message)

@bot.event
async def on_ready():
    print(f'${bot.user} has connected to Discord')

@bot.command(name='stream')
async def stream(ctx):
    await ctx.send('streaming messages from listener')

bot.run(token)
