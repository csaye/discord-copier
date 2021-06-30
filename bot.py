from discord.ext import commands

# read token from file
tokenfile = open('./token.txt')
token = tokenfile.read()
tokenfile.close()

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'${bot.user} has connected to Discord')

@bot.command(name='stream')
async def stream(ctx):
    await ctx.send('streaming messages from listener')

bot.run(token)
