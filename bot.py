import discord

# read token from file
tokenfile = open('./token.txt')
token = tokenfile.read()
tokenfile.close()

client = discord.Client()

@client.event
async def on_ready():
    print(f'${client.user} has connected to Discord')
    for guild in client.guilds:
        if not guild.channels: continue # if no valid channel, continue
        channel = guild.channels[1] # get first channel
        await channel.send('hello world')

client.run(token)
