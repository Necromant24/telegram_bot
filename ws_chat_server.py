import asyncio
import websockets


unauthed_sockets = set()

# support - support client
support = set()

support_client_dict = {}

async def hello(websocket, path):
    print(path)
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")


async def accept(websocket, path):
    print("ok"+path)
    async for message in websocket:
        await websocket.send(message)


    await websocket.send("connected")




start_server = websockets.serve(accept, "localhost", 5500)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()