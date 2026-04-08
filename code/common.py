#!/usr/bin/env python3

import os

import numpy as np
from matplotlib import pyplot as plt

from settings import output_file, X_LABEL, Y_LABEL

def draw_common_chart():
    filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), output_file)
    clusters = np.loadtxt(filepath, dtype='str', delimiter=',', skiprows=0, unpack=False, encoding='utf8')

    if clusters.ndim > 1:
        for cluster in clusters:
            xs = tuple(map(float, cluster[2:4]))
            ys = tuple(map(float, cluster[4:6]))
            
            plt.plot(xs, ys, label=f"{cluster[0]} ({cluster[1]})")
    else:
        plt.plot((float(clusters[2]), float(clusters[3])),\
                 (float(clusters[4]), float(clusters[5])),\
                 label=f"{clusters[0]} ({clusters[1]})")
   
    plt.title("Open and Globular Clusters")
    plt.xlabel(X_LABEL)
    plt.ylabel(Y_LABEL)
    
    ax = plt.gca()

    ax.yaxis.set_inverted(True)

    y_bot, y_top = plt.ylim()
    ax.set_yticks(np.arange(round(y_bot), round(y_top), 0.2), minor=True)
    
    x_bot, x_top = plt.xlim()
    ax.set_xticks(np.arange(round(x_bot), round(x_top), 0.2), minor=True)

    plt.legend()
    plt.show()

if __name__ == '__main__':
    draw_common_chart()
