from os import listdir
from os.path import isfile, join
import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 18888)
    writer.write(message.encode())
    writer.close()
    await asyncio.sleep(5)

# file_path = '50cb2852.json'
# show_grid = '0'
# sleep_time = '1'
# command = file_path + ',' + show_grid + ',' + sleep_time 
# asyncio.run(tcp_echo_client(command))

file_path = './training'
onlyfiles = [join(file_path, f) for f in listdir(file_path) if isfile(join(file_path, f)) ]
for f in onlyfiles:
    print('{}'.format(f))
    show_grid = '0'
    sleep_time = '1'
    command = f + ',' + show_grid + ',' + sleep_time 
    asyncio.run(tcp_echo_client(command))

