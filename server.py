# Copyright (c) Ji Wong Park and its affiliates. All Rights Reserved

import asyncio
from grid import rendering
import pickle
import base64

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    command = message.split(',')
    img_array = rendering(command[0], command[1], float(command[2]) )
    serial_img = pickle.dumps(img_array)
    serial_img = base64.b64encode(serial_img) + b'\n'
    writer.write(serial_img)
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 18888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())

