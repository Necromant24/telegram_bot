import asyncio
import json

import websockets

import bot
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
    email = msg['email']
    ds.add_ws_conn(email, ws)

    some = ws.send("dsfdddddddds")

    await some

    message = json.dumps({'type': 'cmd', 'message': 'connected succsessfully'})
    await ds.send_ws_msg(email, message)

    while True:
        try:
            await ds.send_ws_msg(email, json.dumps({'type': 'ping'}))
        except websockets.exceptions.ConnectionClosed:
            print("Client disconnected.  Do cleanup")
            ds.remove_ws_conn(email)
            break
        await asyncio.sleep(5)


def start_ws_server():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)


    start_server = websockets.serve(initWsConn, "localhost", 5500)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


# import threading
# t1 = threading.Thread(target=bot.start_bot)
#
# t1.start()
#
# start_ws_server()
#
# inp = input("enter any key to close: ")