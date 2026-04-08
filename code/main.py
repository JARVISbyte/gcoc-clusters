import numpy as np
from matplotlib import pyplot as plt

from settings import *


# Data-processing helper-functions
def get_component(x: np.array, y: np.array, slope: float, y_int: float):
    x1 = np.sqrt(np.square(x) + np.square(y - y_int) - np.square(y - slope * x - y_int) / (slope ** 2 + 1))
    signs = ((slope * (y - y_int) + x) >= 0).astype('int') * 2 - 1

    return x1 * signs


def get_x(x1, slope: float):
    return x1 / np.sqrt(1 + slope ** 2)


# load the data from a file
ra, dec, parallax, g_mag, bp_rp = np.loadtxt(filepath, dtype='str', delimiter=',',\
                                             skiprows=1, unpack=True, encoding='utf8')

bp_rp = bp_rp.astype('float')
g_mag = g_mag.astype('float')


# perform calculations
slope, y_int = np.linalg.lstsq(np.vstack([bp_rp, np.ones(len(bp_rp))]).T, g_mag, rcond=None)[0]
x1min, x1max = np.quantile(get_component(bp_rp, g_mag, slope, y_int), (0.2, 0.8))
x_min, x_max = get_x(x1min, slope), get_x(x1max, slope)


# draw the diagram
ax = plt.scatter(bp_rp, g_mag, s=1, c=COLOUR_POINTS).axes

y_bot, y_top = plt.ylim()
ax.set_yticks(np.arange(round(y_bot), round(y_top), 0.2), minor=True)

x_bot, x_top = plt.xlim()
ax.set_xticks(np.arange(round(x_bot), round(x_top), 0.2), minor=True)


plt.plot((x_min, x_max), (slope * x_min + y_int, slope * x_max + y_int), linewidth=2, c=COLOUR_LINE)

ax.xaxis.set_inverted(True)
ax.yaxis.set_inverted(True)

plt.title(OBJECT_TITLE)
plt.xlabel(X_LABEL)
plt.ylabel(Y_LABEL)



plt.show()
