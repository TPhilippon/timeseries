# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:48:00 2015

@author: upression1
"""

import os
import sys
from pyhdf.SD import SD, SDC
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon


l = [2,4,5,7,1,np.nan,3,5,7,np.nan,9,8,6,3,1]

ann = plt.annotate('a point on curve',xy=(np.nan,-1),xytext=(3,-1.3),
... arrowprops=dict(arrowstyle='->'))


plt.show()