#!/usr/bin/env python3

# http tarpit
# 
# stolen from Chris Wellons, wellons@nullprogram.com
# https://nullprogram.com/blog/2019/03/22/

import asyncio
import random

async def handler(_reader, writer):
    writer.write(b'HTTP/1.1 200 OK\r\n')
    try:
        while True:
            await asyncio.sleep(5)
            header = random.randint(0, 2**32)
            value = random.randint(0, 2**32)
            writer.write(b'X-%x: %x\r\n' % (header, value))
            await writer.drain()
    except ConnectionResetError:
        pass

async def main():
    port = 1984
    print("http tarpit, listening at http://127.0.0.1:%d/" % port)
    server = await asyncio.start_server(handler, '0.0.0.0', port)
    async with server:
        await server.serve_forever()

asyncio.run(main())
