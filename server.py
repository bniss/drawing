import asyncio
from grid import rendering

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    command = message.split(',')
    rendering(command[0], command[1], float(command[2]) )

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 18888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())

