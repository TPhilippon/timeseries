# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:32:07 2015

@author: upression1
"""


import os
from Ipython.display import Image
import sys
from pyhdf.SD import SD, SDC   
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
import numpy

     #------------ Choix de la zone d'étude

print "Choix de la zone régionale, patienez..."
m = Basemap(projection='cyl',resolution='c')
m.drawlsmask(land_color='black',ocean_color='None',lakes=True)
img = 'Y:\\SATELITIME\\sdatats\\Graph_data\\V20120012012366.L3m_YR_NPP_CHL_chlor_a_9km.nc.png'
img=Image.open(img)
x=0
y=0
im = plt.imshow(img,extent=(x-180,x+180,y+90,y-90))

plt.show()


print "Entrez vos coordonnées:"
urcrnrlat =raw_input('ymax : ')
llcrnrlat =raw_input('ymin : ')
urcrnrlon =raw_input('xmax : ')
llcrnrlon =raw_input('xmin : ')

i = 1
while i > 0:
    choix =raw_input('Valider o/n?: ')
    
    if choix =="o": 
        
        print "Coordonnées validées."
        i = 0
    else:
        print "recommencez"
        urcrnrlat =raw_input('ymax : ')
        llcrnrlat =raw_input('ymin : ')
        urcrnrlon =raw_input('xmax : ')
        llcrnrlon =raw_input('xmin : ')

ymax = urcrnrlat #Mémoire ZE
ymin = llcrnrlat
xmax = urcrnrlon
xmin = llcrnrlon

    #------------ Choix de la zone d'intérêt
print ("Choix des zones d'intérêt (ZI). Patientez...")

m = Basemap(projection='cyl',llcrnrlat=ymin, urcrnrlat=ymax, llcrnrlon=xmin, urcrnrlon=xmax,resolution='c')
m.drawlsmask(land_color='black',ocean_color='None',lakes=True)

plt.show()

j =raw_input('Combien de ZI à délimiter?: ')
j = int(j)

print "Chargement de la région..."

m = Basemap(projection='cyl',llcrnrlat=ymin, urcrnrlat=ymax, llcrnrlon=xmin, urcrnrlon=xmax,resolution='c')
m.drawlsmask(land_color='black',ocean_color='None',lakes=True)
p = j
i = 0
n = 1       #Compteur pour les max/min coordonnées
d ={}
latmin = 0
latmax = 0
longmin = 0
longmax = 0
while i < j:
    print "ZI restantes:"
    print j
    print "Entrez vos coordonnées:"
    urcrnrlat =raw_input('ymax : ')
    llcrnrlat =raw_input('ymin : ')
    urcrnrlon =raw_input('xmax : ')
    llcrnrlon =raw_input('xmin : ')
    choix =raw_input('Valider o/n?: ')
    
    if choix =="o": 
        
        print "Coordonnées validées."
        j = j - 1
        d['ymax'+str(n)] = urcrnrlat
        d['ymin'+str(n)] = llcrnrlat
        d['xmax'+str(n)] = urcrnrlon
        d['xmin'+str(n)] = llcrnrlon
        
        if latmin < llcrnrlat:
            latmin = llcrnrlat
        if latmax < urcrnrlat:
            latmax = urcrnrlat
        if longmin < llcrnrlon:
            longmin = llcrnrlon
        if longmax < urcrnrlon:
            longmax = urcrnrlon
        
        def draw_screen_poly2( lats2, lons2, m):
            x, y = m( lons2, lats2 )
            xy = zip(x,y)
            poly = Polygon( xy, edgecolor='Red', fill=False, alpha=1.5 )
            plt.gca().add_patch(poly)

        lats2 = [ d["ymin"+str(n)], d["ymax"+str(n)], d["ymax"+str(n)], d["ymin"+str(n)] ]
        lons2 = [ d["xmin"+str(n)], d["xmin"+str(n)], d["xmax"+str(n)], d["xmax"+str(n)] ]
        
        draw_screen_poly2( lats2, lons2, m )
        n = n + 1
    else:
        print "recommencez."
        
def draw_screen_poly( lats, lons, m):
    x, y = m( lons, lats )
    xy = zip(x,y)
    poly = Polygon( xy, edgecolor='Red', fill=False, alpha=1.5 )
    plt.gca().add_patch(poly)

lats = [ latmin-2, latmax+2, latmax+2, latmin-2 ]
lons = [ longmin-2, longmin-2, longmax+2, longmax+2 ]

draw_screen_poly( lats, lons, m )
    
plt.show()


#    #------------ Lecture hdf et Extraction (save)
#
#varnum = 3
#variable = ['nsst_8d', 'pic_8d', 'sst11mic_8d', 'chl_8d'][varnum]
#
#data_out ='Y:\\SATELITIME\\sdatats\\Graph_data\\'   #Win
#data_in ='Y:\\SATELITIME\\ddata\\'+str(variable)+'\\hdf\\'
#
##data_out ='/home/pressions/SATELITIME/sdatats/Graph_data/'   #Unix
##data_in ='/home/pressions/SATELITIME/ddata/'+str(variable)+'/hdf/'
#
#print data_in
#    #nsst_8d  
#    #pic_8d
#    #sst11mic_8d
#    #chl_8d
#
#files = os.listdir(data_in) #Liste les fichiers.
#files.sort() #Trie les fichiers.
#print len(files) #len = longueur de la liste de fichiers.
#
#d2 = {}
#
#
#for myfile in files:
#    
#    print myfile
#    i =1
#    File = SD(data_in+myfile, SDC.READ) #   Lire depuis le hdf.
#    l3 = File.select('l3m_data') #  Et met le contenu dans File.
#    l3d = l3.get() #    Fonction get() pour avoir vraiment le tableau pour lire le hdf.
#    #print 'min/max :', l3d.min(),l3d.max() # On peut demander les valeurs min / max.
#    l3d = np.dot(l3d,1.0)
#    
#    xminZR,xmaxZR=np.sort([abs(xmin*43.2964),abs(xmax*43.2964)])
#    yminZR,ymaxZR=np.sort([abs(ymin*43.2964),abs(ymax*43.2964)])
#    
#    varnum=3  # on a dl plusieurs variables
#    varg=['sst11mic_8d','poc_8d', 'nsst_8d','chl_8d'][varnum]
#    title=[u'Temperature de surface en °C',u'Carbone organique particlaire (POC) en mg.m-3',u'Temperature de surfarce nocturne en °C',u'Chlorophylle en mg.m-3'][varnum]
#    FillValue=[65535.0,-32767.0,-32767.0,-32767.0] # !!!!!!!
#    slI=[(0.00071718,-2),(1,0),(0.00071718,-2),(1,0)][varnum] #varnum récupère pente et intercept. 
#    slope=slI[0] # égal au premier de la paire
#    intercept=slI[1] 
#
#    ScaledDataMinimum= [-2,10,-2,0.01][varnum] # Nous sert dans la formule de convertion. Scaled = données mises à l'échelle.
#    ScaledDataMaximum= [45,1000,45,20][varnum] # Donne les futurs min / max des unités de valeurs.
#
#    vmin=ScaledDataMinimum
#    vmax=ScaledDataMaximum
#
#    ZRl3d=l3d[yminZR:ymaxZR,xminZR:xmaxZR] # Echantilloner. Distance lignes puis colonnes.
#    ZRl3dR=(ZRl3d*slope)+intercept
#    ZRl3dR[ ZRl3dR == FillValue[varnum] ] = np.nan 
#
#    filen = data_out+myfile[0:38]+'_ZR'
#    print filen
#    
#    ZRl3dR = np.array([ZRl3dR]) #str(myfile[:])+'ZR'
#    
#    numpy.save(filen, ZRl3dR)
#    
#
#    while i <= p:
#
#        xminZI,xmaxZI=np.sort([abs(int(d['xmin'+str(i)])*43.2964),abs(int(d['xmax'+str(i)])*43.2964)])
#        yminZI,ymaxZI=np.sort([abs(int(d['ymin'+str(i)])*43.2964),abs(int(d['ymax'+str(i)])*43.2964)])
##        ymaxZI = abs(int(d['ymax'+str(i)])*43.2964)
##        yminZI = abs(int(d['ymin'+str(i)])*43.2964)
##        xmaxZI = abs(int(d['xmax'+str(i)])*43.2964)
##        xminZI = abs(int(d['xmin'+str(i)])*43.2964)
#
##        l3d[ (l3d < vmin) & (l3d != FillValue) ] = vmin #
##        l3d[ l3d > 10 ] = 10.0 #
#        l3d[ l3d == FillValue[varnum] ] = np.nan #0.011 0.00001 #
#
#        ZIl3d=l3d[yminZI:ymaxZI,xmaxZI:xminZI] # Echantilloner la ZI. Distance lignes puis colonnes.
#        ZIl3dR=(ZIl3d*slope)+intercept
#        #ZIl3dR=np.dot(ZIl3dR,1.0) #   
#
#        filen = data_out+myfile[0:38]+'_ZI'  #'A'+str(a)+str(format(day,'03'))+str(a)+str(format(day2,'03'))+'.'+varg+
#        print filen+str(i)
#        
#        np.array([ZIl3dR])
#        
#        
#        numpy.save(filen+str(i), ZIl3dR)
#        
#
#        
#        
#        i=i+1                

    


print 'Fin'
