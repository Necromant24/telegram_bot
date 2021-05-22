import asyncio
import json

import websockets
import data_structs as ds


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



#unused
async def accept(websocket, path):
    print("ok"+path)
    async for message in websocket:

        msg = json.loads(message)




        await websocket.send(message)


    await websocket.send("connected")





async def initWsConn(ws, path):

    ws_msg = await ws.recv()
    msg = json.loads(ws_msg)

    ds.addWsConn(msg['from'], msg['email_or_name'], ws )

    await ws.send('connected succsessfully')


start_server = websockets.serve(initWsConn, "localhost", 5500)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()