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
import numpy


data_out ='/home/pressions/SATELITIME/sdatats/Graph_data/'

files = os.listdir(data_out) #Liste les fichiers.
files.sort() #Trie les fichiers.

a = 2002
day = 185
day2 = day+7
varg = 'chl_8d'

filen = data_out+'A'+str(a)+str(format(day,'03'))+str(a)+str(format(day2,'03'))+'.'+varg+'_ZI'


f = filen+str(i)+'.npy'
np.arrray([f])
data = numpy.load(f)
numpy.mean(data)

plt.plot(data,'o')
    
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trace test')

plt.show()