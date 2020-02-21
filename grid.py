# Copyright (c) Ji Wong Park, Inc. and its affiliates. All Rights Reserved

import matplotlib.pyplot as plt
import matplotlib.colors as clr
import numpy as np
import json


def show_grid(np_array):
    array_shape = np_array.shape
    x = array_shape[0]
    y = array_shape[1]

    # make a figure + axes
    fig, ax = plt.subplots(1, 1, tight_layout=True)

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

    # draw the boxes
    ax.imshow(np_array, interpolation='none', cmap=my_cmap, norm=my_norm, extent=[0, y, 0, x], zorder=0)

    # turn off the axis labels
    ax.axis('off')

    plt.show()


def read_json(file_path):
    with open(file_path) as json_data:
        return json.load(json_data)


def main():
    print('version: {}'.format(0))

    # file_path = '007bbfb7.json'
    file_path = 'f2829549.json'

    data = read_json(file_path)

    print('test input: {}'.format(data['test'][0]['input']))

    print('------------------------------')

    print('length: {}'.format(len(data['train'])))

    # print('train input: {}'.format(data['train'][0]['input']))

    np_input_data = np.array( data['train'][0]['input'] )
    print('train input: {}'.format(np_input_data))

    print('train input shape: {}'.format(np_input_data.shape))

    print('------------------------------')

    np_output_data = np.array( data['train'][0]['output'] )
    print('train output: {}'.format(np_output_data))
    print('train output shape: {}'.format(np_output_data.shape))

    show_grid(np_input_data)
    # show_grid(np_output_data)

if __name__ == '__main__': main()
