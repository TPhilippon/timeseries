# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 14:20:45 2015

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


     #------------ Choix de la zone d'étude

#print "Choix de la zone régionale, patienez..."
##m = Basemap(projection='cyl',resolution='c')
##m.drawlsmask(land_color='black',ocean_color='None',lakes=True)
#
##plt.show()
#
#print "Entrez vos coordonnées:"
#urcrnrlat =raw_input('ymax : ')
#llcrnrlat =raw_input('ymin : ')
#urcrnrlon =raw_input('xmax : ')
#llcrnrlon =raw_input('xmin : ')
#
#i = 1
#while i > 0:
#    choix =raw_input('Valider o/n?: ')
#    
#    if choix =="o": 
#        
#        print "Coordonnées validées."
#        i = 0
#    else:
#        print "recommencez"
#        urcrnrlat =raw_input('ymax : ')
#        llcrnrlat =raw_input('ymin : ')
#        urcrnrlon =raw_input('xmax : ')
#        llcrnrlon =raw_input('xmin : ')
#
#ymax = urcrnrlat #Mémoire ZR
#ymin = llcrnrlat
#xmax = urcrnrlon
#xmin = llcrnrlon

ymax=30
ymin=-7
xmax=-33
xmin=-100


    #------------ Lecture hdf et Extraction (npy save)

data_out ='/home/pressions/SATELITIME/sdatats/Graph_data/'
data_in ='/home/pressions/SATELITIME/ddata/'+'chl_8d'+'/hdf/'
    #nsst_8d
    #pic_8d
    #sst11mic_8d
    #chl_8d

files = os.listdir(data_in) #Liste les fichiers.
files.sort() #Trie les fichiers.
print len(files) #len = longueur de la liste de fichiers.
x =1

for myfile in files:

    File = SD(data_in+myfile, SDC.READ) #   Lire depuis le hdf.
    l3 = File.select('l3m_data') #  Et met le contenu dans File.
    l3d = l3.get() #    tableau pour lire le hdf.
    print 'min/max :', l3d.min(),l3d.max() # valeurs min / max.
    print l3d.shape
    
    l3d=np.dot(l3d,1.0) #   CRUCIAL : transformation en objet numpy pour manipuler plus facilement    
    print 'min/max :', l3d.min(),l3d.max()    
    
    ymaxZR = abs(int(ymax)*43.2964)
    yminZR = abs(int(ymin)*43.2964)
    xmaxZR = abs(int(xmax)*43.2964)
    xminZR = abs(int(xmin)*43.2964)
    
    varnum=3  # on a dl plusieurs variables
    varg=['sst11mic_8d','poc_8d', 'nsst_8d','chl_8d'][varnum]
    title=[u'Temperature de surface en °C',u'Carbone organique particlaire (POC) en mg.m-3',u'Temperature de surfarce nocturne en °C',u'Chlorophylle en mg.m-3'][varnum]
    FillValue=[65535.0,-32767.0,-32767.0,-32767.0]
    slI=[(0.00071718,-2),(1,0),(0.00071718,-2),(1,0)][varnum] #varnum récupère pente et intercept. 
    slope=slI[0] # égal au premier de la paire
    intercept=slI[1] 

    ScaledDataMinimum= [-2,10,-2,0.01][varnum] # Nous sert dans la formule de convertion. Scaled = données mises à l'échelle.
    ScaledDataMaximum= [45,1000,45,20][varnum] # Donne les futurs min / max des unités de valeurs.

    vmin=ScaledDataMinimum
    vmax=ScaledDataMaximum

    l3d[ (l3d < vmin) & (l3d != FillValue) ] = vmin #
    l3d[ l3d > 10 ] = 10.0 #
    l3d[ l3d == 65535.0 ] = np.nan #0.011 0.00001 #

    ZRl3d=l3d[yminZR:ymaxZR,xmaxZR:xminZR] # Echantilloner. Distance lignes puis colonnes.
#    print 'min/max :', ZRl3d.min(),ZRl3d.max()
    ZRl3dR=(ZRl3d*slope)+intercept
#    print 'min/max :', ZRl3dR.min(),ZRl3dR.max()

    ZRl3d[ (ZRl3d < vmin) & (ZRl3d != FillValue) ] = vmin
    ZRl3d[ ZRl3d > vmax ] = vmax
    ZRl3d[ ZRl3d == FillValue ] = 0.00001
    


#    print 'min/max :', l3d.min(),l3d.max()

    filen = data_out+myfile[0:38]+'_ZR'
    print filen
    
    #np.array([ZRl3dR])
    
    numpy.save(filen, ZRl3dR)

    
    
    
print 'Fin'