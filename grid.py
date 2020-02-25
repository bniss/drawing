# Copyright (c) Ji Wong Park and its affiliates. All Rights Reserved

import matplotlib.pyplot as plt
import matplotlib.colors as clr
import numpy as np
import json
from time import sleep

run_once = 0 

# make a figure + axes
fig = plt.figure(1)
ax = fig.add_subplot(121)
# win = fig.canvas.manager.window

ax_out = fig.add_subplot(122)

plt.ion()


# def init_grid():
#     run_once = 0 
im = None
im_out = None

def show_grid(np_array, np_out_array):
    global run_once, im

    # if run_once == 1:
    #     plt.close()

    array_shape = np_array.shape
    x = array_shape[0]
    y = array_shape[1]

    array_out_shape = np_out_array.shape
    x_out = array_out_shape[0]
    y_out = array_out_shape[1]

    # make color map
    my_cmap = clr.ListedColormap(['#000000', '#0074D9', '#FF4136', '#2ECC40', '#FFDC00', '#AAAAAA', '#F012BE', '#FF851B', '#7FDBFF', '#870C25'])

    # set the 'bad' values (nan) to be white and transparent
    my_cmap.set_bad(color='w', alpha=0)

    bound = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_norm = clr.BoundaryNorm(bound, my_cmap.N, clip=True)

    # # draw the grid
    for i in range(x + 1):
        ax.axhline(i, lw=2, color='k', zorder=5)

    for j in range(y + 1):
        ax.axvline(j, lw=2, color='k', zorder=5)
        ax_out.axvline(j, lw=2, color='k', zorder=5)

    for i in range(x_out + 1):
        ax_out.axhline(i, lw=2, color='k', zorder=5)

    for j in range(y_out + 1):
        ax_out.axvline(j, lw=2, color='k', zorder=5)

    # draw the boxes
    im = ax.imshow(np_array, interpolation='none', cmap=my_cmap, norm=my_norm, extent=[0, y, 0, x], zorder=0)
 
    im_out = ax_out.imshow(np_out_array, interpolation='none', cmap=my_cmap, norm=my_norm, extent=[0, y_out, 0, x_out], zorder=0)

    if run_once == 0:
        run_once = 1 

        # turn off the axis labels
        ax.axis('off')
        ax_out.axis('off')

        print('client A request')
        # make a figure + axes
        # fig, ax = plt.subplots(1, 1, tight_layout=True)
        fig.show()
        fig.canvas.draw()
        fig.canvas.flush_events()

        plt.show()
    else:
        print('client B, C, D, ... request')
        # im.set_array(np_array.ravel())
        im.set_array(np_array)
        im_out.set_array(np_out_array)
        fig.show()
        fig.canvas.draw()
        fig.canvas.flush_events()

        plt.draw()

def read_json(file_path):
    with open(file_path) as json_data:
        return json.load(json_data)


def rendering(file_path, train_type, in_out):
    data = read_json(file_path)

    # train_type - 0: 'train', 1: 'test'
    # in_out     - 0: input,   1: output

    val_train = 'train'
    val_in_out = 'input'

    if in_out != 0:
        val_in_out = 'output'

    if train_type != 0:
        val_train = 'test'

    # print('length: {}'.format(len(data['train'])))
    length = len(data['train'])

    for i in range(length):
        np_data = np.array( data[val_train][i]['input'] )
        np_out_data = np.array( data[val_train][i]['output'] )
        show_grid(np_data, np_out_data)
        sleep(0.5)

def main():
    print('version: {}'.format(0))

    train_type = 0
    in_out = 0
    # # file_path = '007bbfb7.json'
    file_path = 'f2829549.json'

    # rendering(file_path, train_type, in_out)

    # data = read_json(file_path)

    # print('test input: {}'.format(data['test'][0]['input']))

    # print('------------------------------')

    # print('length: {}'.format(len(data['train'])))

    # # print('train input: {}'.format(data['train'][0]['input']))

    # np_input_data = np.array( data['train'][0]['input'] )
    # print('train input: {}'.format(np_input_data))

    # print('train input shape: {}'.format(np_input_data.shape))

    # print('------------------------------')

    # np_output_data = np.array( data['train'][0]['output'] )
    # print('train output: {}'.format(np_output_data))
    # print('train output shape: {}'.format(np_output_data.shape))

    # show_grid(np_input_data)
    # # show_grid(np_output_data)

if __name__ == '__main__': main()
