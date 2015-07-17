#!/usr/bin/env python
# -*- coding: utf8 -*-
#           ** Conversion ZR en .png **
# ** Valable pour SWf et MODIs en 4km et 9km **
#################################################################################
# Conversion des ZR en fichiers PNG pour affichage / video / ou autre traitement
# d'image. 
# 
# Remarques :
# Variables 'reso', 'varg', et 'sensor' modifiables.
# Les coordonnées de ZR sont à modifier suivant qu'on est en 9 ou 4km.
# ===============================================================================
# =========================== Imports ===========================================
import os
import sys
import numpy as np
from pyhdf.SD import SD, SDC
from mpl_toolkits.basemap import Basemap, cm
from matplotlib.colors import LogNorm
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.signal
# =======================================================================
# ========================= Variables ===================================

vmin,vmax=0.01,20
#xzrmin,xzrmax,yzrmin,yzrmax=2500,3500,1500,2200                     # Coordonnées de ZR 4km
#xzrmin,xzrmax,yzrmin,yzrmax=1250,1750,750,1100                      # Coordonnées de ZR 9km

# Suivant : pour pouvoir convertir.
varnum=3 
interpolation= 'interpolated/'                                                # 'simple/' ou 'interpolated/' <- sans ou avec interpolation
reso= '9km'
sensor='aqua'                                                                 # choose between'aqua' and 'swf'
#varg=['sst11mic_8d','poc_8d', 'nsst_8d','chl_8d','pic_8d'][varnum]           # --> 8D
varg=['sst11mic_32d','poc_32d', 'nsst_32d','chl_32d','pic_32d'][varnum]       # --> 32D

title=[u'Temperature de surface en °C',u'Carbone organique particlaire (POC) en mg.m-3',u'Temperature de surfarce nocturne en °C',u'Chlorophylle en mg.m-3'][varnum]
slI=[(0.00071718,-2),(1,0),(0.00071718,-2),(1,0)][varnum] # cette fois varnum récupère pente et intercept. 
slope=slI[0] # égal au premier de la paire slI[varnum]
intercept=slI[1] 

#colors = [(0.33,0.33,0.33)] + [(plt.cm.jet(i)) for i in xrange(1,256)]
#norm=mpl.colors.LogNorm(vmin=vmin, vmax=vmax)
#new_map = matplotlib.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256) # Colormap

#norm=[mpl.colors.Normalize(vmin=ScaledDataMinimum, vmax=ScaledDataMaximum),mpl.colors.LogNorm(vmin=ScaledDataMinimum,vmax=ScaledDataMaximum), \
#      mpl.colors.Normalize(vmin=ScaledDataMinimum, vmax=ScaledDataMaximum),mpl.colors.LogNorm(vmin=ScaledDataMinimum, vmax=ScaledDataMaximum)][varnum]


norm=mpl.colors.LogNorm(vmin=vmin, vmax=vmax)
colors = [(0.33,0.33,0.33)] + [(plt.cm.jet(i)) for i in xrange(1,256)]
new_map = mpl.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256) # Colormap

path = '/home/pressions/SATELITIME/data/ZR/'+sensor+'/'+varg+'/'+reso+'/'
pathPNG = '/home/pressions/SATELITIME/data/PNG/'+sensor+'/'+varg+'/'+reso+'/png_caraibe/'+interpolation

# ========================================================================
# ---------- read data ---------- #
files = os.listdir(path)    #Liste ldes fichiers.
files.sort()                #Trie les fichiers.
print len(files)            #len = longueur de la liste de fichiers.

# -------------------------------------------------------
                                        
for myfile in files:

    annee = myfile[1:5]
    j = int(myfile[12:15])
    j=int(j)
 
    if j >= 355 or j < 83:
        saison = u'Hiver'
    if j >= 83 and j < 176:
        saison = u'Printemps'
    if j >= 176 and j < 261:
        saison = u'Eté'
    if j >= 261 and j < 355:
        saison = u'Automne'

    l3d=np.load(path+myfile)    

    print myfile,annee,j,np.nanmin(l3d),np.nanmax(l3d) # On peut demander les valeurs min / max.

    #------------ Interpolation
    data = l3d
    if interpolation == 'interpolated/':
        print 'interpolating....'
        # a boolean array of (width, height) which False where there are missing values and True where there are valid (non-missing) values
        mask = np.isnan(data)
        mymask=mask    
        mask=~mask
        # array of (number of points, 2) containing the x,y coordinates of the valid values only
        xx, yy = np.meshgrid(np.arange(data.shape[1]), np.arange(data.shape[0]))
        xym = np.vstack( (np.ravel(xx[mask]), np.ravel(yy[mask])) ).T
        # the valid values in the first, second, third color channel,  as 1D arrays (in the same order as their coordinates in xym)
        data1 = np.ravel( data[mask] )
        # three separate interpolators for the separate color channels
        interp0 = scipy.interpolate.NearestNDInterpolator( xym, data1 )
        # interpolate the whole image, one color channel at a time    
        result0 = interp0(np.ravel(xx), np.ravel(yy)).reshape( xx.shape )
        l3d=result0
        print 'end interp' 
        
        l3d=l3d*slope+intercept
    
    #---------- Plot Data Global Map ----------#
    fig=plt.figure()
    ax = fig.add_subplot(1,1,1)
    c = ax.pcolormesh(X, Y, weighted_temperature)
    #img= plt.imshow(np.flipud(l3d), norm=norm, cmap=new_map , interpolation='bilinear') # plt.get_cmap('gray') #vmin=ScaledDataMinimum, vmax=ScaledDataMaximum,
#    plt.imshow(data,norm=norm,origin='upper', cmap=new_map,interpolation='none',aspect='equal') #

    plt.imshow(l3d,norm=norm, origin='upper', cmap=new_map)
    
#    plt.imshow(data,norm=norm,extent=[xzrmin,xzrmax,yzrmin,yzrmax],origin='upper', cmap=new_map) #
    
    #cb.set_label(title)
    plt.title(saison+'   '+annee+'   jour : '+str(j))
    print pathPNG+myfile
    
    plt.savefig(pathPNG+myfile[0:41]+'.png',dpi=200,bbox_inches='tight')
    plt.imshow(np.zeros(np.shape(l3d)), cmap=plt.get_cmap('Greys'))             ### --> Matrice vide pour reset image (sinon superposition)
#    plt.show()
    sys.exit()
plt.close()

print 'fin'
