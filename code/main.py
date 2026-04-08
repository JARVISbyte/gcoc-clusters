#!/usr/bin/env python3

import os

import numpy as np
from matplotlib import pyplot as plt

from settings import *


# Math helper-functions
def project_on_line(x: np.array, y: np.array, slope: float, y_int: float):
    x1 = np.sqrt(np.square(x) + np.square(y - y_int) - np.square(y - slope * x - y_int) / (slope ** 2 + 1))
    signs = ((slope * (y - y_int) + x) >= 0).astype('int') * 2 - 1

    return x1 * signs


def project_from_line(x1, slope: float):
    return x1 / np.sqrt(1 + slope ** 2)


def load_data(filename):
    filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', filename)
    ra, dec, parallax, g_mag, bp_rp = np.loadtxt(filepath, dtype='str', delimiter=',', skiprows=1, unpack=True, encoding='utf8')
    return g_mag.astype('float'), bp_rp.astype('float')

def simplify_cluster(g_mag: np.array, bp_rp: np.array):
    # perform calculations
    slope, y_int = np.linalg.lstsq(np.vstack([bp_rp, np.ones(len(bp_rp))]).T, g_mag, rcond=None)[0]
    x1min, x1max = np.quantile(project_on_line(bp_rp, g_mag, slope, y_int), (0.2, 0.8))
    x_min, x_max = project_from_line(x1min, slope), project_from_line(x1max, slope)

    y_min, y_max = slope * x_min + y_int, slope * x_max + y_int

    return x_min, x_max, y_min, y_max

# draw the chart 
def draw_chart(g_mag: np.array, bp_rp: np.array, fit_params: tuple[float, float, float, float]=None):
    ax = plt.scatter(bp_rp, g_mag, s=1, c=COLOUR_POINTS).axes
    
    # add approximate fit to the chart
    if fit_params:
        plt.plot(fit_params[0:2], fit_params[2:4], linewidth=2, c=COLOUR_LINE)

    # setting the chart
    plt.title(OBJECT_TITLE)
    plt.xlabel(X_LABEL)
    plt.ylabel(Y_LABEL)
    
    ax.yaxis.set_inverted(True)

    y_bot, y_top = plt.ylim()
    ax.set_yticks(np.arange(round(y_bot), round(y_top), 0.2), minor=True)

    x_bot, x_top = plt.xlim()
    ax.set_xticks(np.arange(round(x_bot), round(x_top), 0.2), minor=True)

    # showing the chart
    plt.show()

def export(output_filename, fit_params):
    filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), output_filename)
    with open(filepath, 'a') as file:
        print(OBJECT_TITLE, OBJECT_TYPE, *fit_params, sep=',', file=file) 

if __name__ == '__main__':
    g_mag, bp_rp = load_data(filepath)
    fit_params = simplify_cluster(g_mag, bp_rp)
    draw_chart(g_mag, bp_rp, fit_params)
    export(output_file, fit_params)
