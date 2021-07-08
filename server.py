import discord, asyncio, websockets, datetime, threading

# read token from file
tokenfile = open('./token.txt')
TOKEN = tokenfile.read()
tokenfile.close()

client = discord.Client()
general = None

# find general channel on start
@client.event
async def on_ready():
    global general
    print(f'{client.user} has connected to Discord')
    # get general channel
    for channel in client.get_all_channels():
        if channel.name == "general":
            general = channel
            break

# handle received message
async def handler(websocket, path):
    global general
    message = await websocket.recv()
    print(f'Received message {message}')
    if general: await general.send(message)

start_server = websockets.serve(handler, "localhost", 9999)

# initialize bot and server
loop = asyncio.get_event_loop()
loop.create_task(client.start(TOKEN))
loop.run_until_complete(start_server)
threading.Thread(target=loop.run_forever).start()
