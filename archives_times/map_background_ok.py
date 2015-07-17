# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:15:16 2015

@author: upression1
"""
import os,sys
from pyhdf.SD import SD, SDC   
#from mpl_toolkits.basemap import Basemap
from pylab import mpl as mpl
import matplotlib.pyplot as plt
import numpy as np

# =========================

xzrmin,xzrmax,yzrmin,yzrmax=1250,1750,750,1100                          # ZR pour 9km
#xzrmin,xzrmax,yzrmin,yzrmax=2500,3500,1500,2200                        # ZR pour 4km


imfile = '/home/pressions/SATELITIME/data/Chl2009_9km.hdf'          # Image pour voir les pixels (choisir la bonne résolution)

fzr = SD(imfile, SDC.READ)      #  Lire depuis le hdf.
data = fzr.select('l3m_data')   #  choisit le hdf datasets

norm=mpl.colors.LogNorm(vmin=0.01, vmax=20)
colors = [(0.33,0.33,0.33)] + [(plt.cm.jet(i)) for i in xrange(1,256)]
new_map = mpl.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256) # Colormap
colors = [(0.33,0.33,0.33)] + [(plt.cm.gray(i)) for i in xrange(1,256)]
new_map_gray = mpl.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256) # Colormap

data = data.get()               #  Fonction get() pour avoir vraiment le tableau pour lire le hdf.
#data = np.dot(data,1.0)

zr=data[yzrmin:yzrmax,xzrmin:xzrmax]
#plt.imshow(zr,norm=norm,extent=[xzrmin,xzrmax,yzrmin,yzrmax],origin='lower', cmap=new_map,interpolation='none',aspect='equal') #
#plt.gca().invert_yaxis()

bakmap = data
bakmap[ bakmap != -32767.] = 0
bakmap[ bakmap == -32767.] = np.nan    



plt.show()


