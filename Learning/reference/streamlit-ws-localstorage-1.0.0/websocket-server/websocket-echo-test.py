import asyncio
import websockets


def main():
    async def query(future):
        async with websockets.connect("ws://localhost:8005/?uid=84651289465") as ws:
            await ws.send('{"cmd":"echo","msg":"hi4"}')
            response = await ws.recv()
            print('response: ', response)
            future.set_result(response)

    future1 = asyncio.Future()
    asyncio.get_event_loop().run_until_complete(query(future1))
    print('future1.result: ', future1.result())


main()