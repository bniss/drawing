import matplotlib.pyplot as plt
import matplotlib.colors as clr
import numpy as np

def show_grid(x, y):
    # make an empty data set
    data = np.ones((x, y)) * np.nan
    # fill in some fake data
    for j in range(3)[::-1]:
        data[x//2 - j : x//2 + j +1, x//2 - j : x//2 + j +1] = j

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
    ax.imshow(data, interpolation='none', cmap=my_cmap, extent=[0, y, 0, x], zorder=0)
    # turn off the axis labels
    ax.axis('off')

    plt.rc('grid', linestyle="-", color='black')
    # plt.scatter(x, y)
    plt.grid(True)
    plt.show()

def main():
    print('version: {}'.format(0))
    show_grid(4, 18)

if __name__ == '__main__': main()
