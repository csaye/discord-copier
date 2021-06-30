import discord

# read token from file
tokenfile = open('./token.txt')
token = tokenfile.read()
tokenfile.close()

client = discord.Client()

client.run(token)
