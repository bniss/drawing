from os import listdir
from os.path import isfile, join
from time import sleep

import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 18888)

    print(f'Send: {message!r}')
    writer.write(message.encode())

    # data = await reader.read(100)
    # print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()

# file_path = '007bbfb7.json'
# file_path = 'f2829549.json'
# train_type = '0'
# in_out = '0'
# command = file_path + ',' + train_type + ',' + in_out


file_path = './training'

onlyfiles = [join(file_path, f) for f in listdir(file_path) if isfile(join(file_path, f)) ]

for f in onlyfiles:
    # print('{}'.format(f))
    train_type = '0'
    in_out = '0'
    command = f + ',' + train_type + ',' + in_out
    asyncio.run(tcp_echo_client(command))
    sleep(1)

