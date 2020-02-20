import matplotlib.pyplot as plt
import matplotlib.colors as clr
import numpy as np
import json


def show_grid(np_array):
    array_shape = np_array.shape
    x = array_shape[0]
    y = array_shape[1]

    # # make an empty data set
    # data = np.ones((x, y)) * np.nan
    # # fill in some fake data
    # for j in range(3)[::-1]:
    #     data[x//2 - j : x//2 + j +1, x//2 - j : x//2 + j +1] = j

    # make a figure + axes
    fig, ax = plt.subplots(1, 1, tight_layout=True)
    # make color map
    my_cmap = clr.ListedColormap(['r', 'g', 'b'])
    # set the 'bad' values (nan) to be white and transparent
    my_cmap.set_bad(color='w', alpha=0)

    # # draw the grid
    for i in range(x + 1):
        ax.axhline(i, lw=2, color='k', zorder=5)

    for j in range(y + 1):
        ax.axvline(j, lw=2, color='k', zorder=5)

    # draw the boxes
    ax.imshow(np_array, interpolation='none', cmap=my_cmap, extent=[0, y, 0, x], zorder=0)
    # turn off the axis labels
    ax.axis('off')

    plt.show()


def read_json(file_path):
    with open(file_path) as json_data:
        return json.load(json_data)


def main():
    print('version: {}'.format(0))

    file_path = '007bbfb7.json'

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
    print('train output shape: {}'.format(np_output_data.shape))

    show_grid(np_input_data)

if __name__ == '__main__': main()
