# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 11:17:00 2015

@author: pam
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:32:07 2015
@author: Terence, Pierre-Alain, UMR
"""
import os,sys
from pyhdf.SD import SD, SDC   
from mpl_toolkits.basemap import Basemap
from pylab import mpl as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
# =========================== Definition Varaibles =======================
varnum = 3
variable = ['nsst_8d', 'pic_8d', 'sst11mic_8d', 'chl_8d'][varnum]
bzi=1000 # marge autour des ZI pour la zoom
#data_out ='Y:\\home\\pressions\\SATELITIME\\sdatats\\Graph_data\\'   #Win
#data_indd ='Y:\\SATELITIME\\ddata\\'+str(variable)+'\\hdf'
data_out1 ='/home/pressions/SATELITIME/sdatats/Graph_data/ZR/' 
data_out2 ='/home/pressions/SATELITIME/sdatats/Graph_data/ZI/'  #Unix
data_in ='/home/pressions/SATELITIME/ddata/'+str(variable)+'/hdf/'
imfile = '/home/pressions/SATELITIME/data/chl2009.hdf' 

xzrmin,xzrmax,yzrmin,yzrmax=2300,2500,800,1000


#xzrmin,xzrmax,yzrmin,yzrmax=2800,2900,1500,1900

norm=mpl.colors.LogNorm(vmin=0.01, vmax=20)
colors = [(0.33,0.33,0.33)] + [(plt.cm.jet(i)) for i in xrange(1,256)]
new_map = mpl.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256) # Colormap

# ========================================================================
print "Choix de la zone régionale, patienez..."

fzr = SD(imfile, SDC.READ) #   Lire depuis le hdf.
dzr = fzr.select('l3m_data') #  Et met le contenu dans File.
dzr = dzr.get() #    Fonction get() pour avoir vraiment le tableau pour lire le hdf.
#dzr = np.dot(dzr,1.0)

yzrmin,yzrmax,xzrmin,xzrmax=0,4320,00,8640
zr=dzr[yzrmin:yzrmax,xzrmin:xzrmax]
plt.imshow(zr,norm=norm,extent=[xzrmin,xzrmax,yzrmin,yzrmax],origin='lower', cmap=new_map,interpolation='none',aspect='equal') #extent=ezr
plt.gca().invert_yaxis()
plt.show()

yzrmin,yzrmax,xzrmin,xzrmax=00,1000,500,3000
zr=dzr[yzrmin:yzrmax,xzrmin:xzrmax]
plt.imshow(zr,norm=norm,extent=[xzrmin,xzrmax,yzrmin,yzrmax],origin='lower', cmap=new_map,interpolation='none',aspect='equal') #extent=ezr
plt.gca().invert_yaxis()
plt.show()


yzrmin,yzrmax,xzrmin,xzrmax=1500,2500,2000,4000
zr=dzr[yzrmin:yzrmax,xzrmin:xzrmax]
plt.imshow(zr,norm=norm,extent=[xzrmin,xzrmax,yzrmin,yzrmax],origin='lower', cmap=new_map,interpolation='none',aspect='equal') #extent=ezr
plt.gca().invert_yaxis()
plt.show()

yzrmin,yzrmax,xzrmin,xzrmax=1500,1900,2800,2900
zr=dzr[yzrmin:yzrmax,xzrmin:xzrmax]
plt.imshow(zr,norm=norm,extent=[xzrmin,xzrmax,yzrmin,yzrmax],origin='lower', cmap=new_map,interpolation='none',aspect='equal') #extent=ezr
plt.gca().invert_yaxis()
plt.show()


