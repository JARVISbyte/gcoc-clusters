#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt

from settings import output_file

def draw_common_chart():
    clusters = np.loadtxt(output_file, dtype='str', delimiter=',', skiprows=0, unpack=False, encoding='utf8')

    if clusters.ndim > 1:
        for cluster in clusters:
            xs = tuple(map(float, cluster[1:3]))
            ys = tuple(map(float, cluster[3:5]))
            print(xs, ys)
            plt.plot(xs, ys, label=cluster[0])
    else:
        plt.plot((float(clusters[1]), float(clusters[2])),\
                 (float(clusters[3]), float(clusters[4])),\
                 label=clusters[0])

    plt.show()

if __name__ == '__main__':
    draw_common_chart()
