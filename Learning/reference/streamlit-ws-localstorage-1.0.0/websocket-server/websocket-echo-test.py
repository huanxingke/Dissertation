import asyncio
import ssl

import certifi
import websocket
import websockets


def main():
    ssl_context = ssl.create_default_context()
    ssl_context.load_verify_locations(certifi.where())

    async def query(future):
        async with websockets.connect("wss://127.0.0.1:8001/?uid=21", ssl=ssl_context) as ws:
            await ws.send('{"cmd":"echo","msg":"hi4"}')
            response = await ws.recv()
            print('response: ', response)
            future.set_result(response)

    future1 = asyncio.Future()
    asyncio.get_event_loop().run_until_complete(query(future1))
    print('future1.result: ', future1.result())


main()