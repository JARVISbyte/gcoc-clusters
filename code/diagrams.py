#!usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt

bp_rp, mag_g, parallax, radvel, ra, dec, ang_sep = np.loadtxt('../data/m6-open.csv', dtype='str', delimiter=',', \
                                                              skiprows=1, unpack=True, encoding='utf8')

bp_rp = bp_rp.astype('float')
mag_g = mag_g.astype('float')

plt.scatter(bp_rp, mag_g, s=1, c='r')
plt.gca().yaxis.set_inverted(True)



plt.show()
