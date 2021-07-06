import asyncio, websockets, datetime

async def handler(websocket, path):
    message = await websocket.recv()
    print(f'received message {message}')
    f = open('./message.txt', 'w')
    timestamp = datetime.datetime.now()
    f.write(f'{timestamp}\n{message}')
    f.close()

start_server = websockets.serve(handler, "localhost", 9999)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
