# Copyright (c) Ji Wong Park and its affiliates. All Rights Reserved

from os import listdir
from os.path import isfile, join
import asyncio
import io
import pickle
import base64

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 18888)
    writer.write(message.encode())
    data = await reader.read()

    img_data = base64.b64decode(data[:-1])
    img_array = pickle.loads(img_data)

    writer.close()
    await asyncio.sleep(5)
    return img_array

# file_path = './training/50cb2852.json'
# show_grid = '0'
# sleep_time = '1'
# command = file_path + ',' + show_grid + ',' + sleep_time 
# asyncio.run(tcp_echo_client(command))

file_save = True 
file_count = 0
file_path = './training'
onlyfiles = [join(file_path, f) for f in listdir(file_path) if isfile(join(file_path, f)) ]
for f in onlyfiles:
    print('{}'.format(f))
    show_grid = '0'
    sleep_time = '1'
    command = f + ',' + show_grid + ',' + sleep_time 

    if file_save:
        # save png file from img_array
        img_array = asyncio.run(tcp_echo_client(command))
        for img in img_array:
            fn = str(file_count) + ".png"
            out_file = open(fn, "wb")
            out_file.write(img)
            out_file.close()
            file_count += 1
    else:
        # only show images
        asyncio.run(tcp_echo_client(command))

