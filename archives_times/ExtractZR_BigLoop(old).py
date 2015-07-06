# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:32:07 2015

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

print "Choix de la zone régionale, patienez..."
#m = Basemap(projection='cyl',resolution='c')
#m.drawlsmask(land_color='black',ocean_color='None',lakes=True)

#plt.show()

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
#ymax = urcrnrlat #Mémoire ZE
#ymin = llcrnrlat
#xmax = urcrnrlon
#xmin = llcrnrlon

    #------------ Choix de la zone d'intérêt
print ("Choix des zones d'intérêt (ZI). Patientez...")

#m = Basemap(projection='cyl',llcrnrlat=ymin, urcrnrlat=ymax, llcrnrlon=xmin, urcrnrlon=xmax,resolution='c')
#m.drawlsmask(land_color='black',ocean_color='None',lakes=True)
#
#plt.show()

j =raw_input('Combien de ZI à délimiter?: ')
j = int(j)

print "Chargement de la mappe monde..."

#m = Basemap(projection='cyl',resolution='c')
#m.drawlsmask(land_color='black',ocean_color='None',lakes=True)
p = j
i = 0
n = 1       #Compteur pour les max/min coordonnées
d ={}
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

#        def draw_screen_poly2( lats2, lons2, m):
#            x, y = m( lons2, lats2 )
#            xy = zip(x,y)
#            poly = Polygon( xy, edgecolor='Yellow', fill=False, alpha=1.5 )
#            plt.gca().add_patch(poly)
#
#        lats2 = [ d["ymin"+str(n)], d["ymax"+str(n)], d["ymax"+str(n)], d["ymin"+str(n)] ]
#        lons2 = [ d["xmin"+str(n)], d["xmin"+str(n)], d["xmax"+str(n)], d["xmax"+str(n)] ]
#
#        draw_screen_poly2( lats2, lons2, m )
        n = n + 1
    else:
        print "recommencez."
        
#def draw_screen_poly( lats, lons, m):
#    x, y = m( lons, lats )
#    xy = zip(x,y)
#    poly = Polygon( xy, edgecolor='Red', fill=False, alpha=1.5 )
#    plt.gca().add_patch(poly)
#
#lats = [ ymin, ymax, ymax, ymin ]
#lons = [ xmin, xmin, xmax, xmax ]
#
#draw_screen_poly( lats, lons, m )
#    
#plt.show()

    #------------ Lecture hdf et Extraction (save)

data_out ='/home/pressions/SATELITIME/sdatats/Graph_data/'
data_in ='/home/pressions/SATELITIME/ddata/'+'chl_8d'+'/hdf/'
    #nsst_8d
    #pic_8d
    #sst11mic_8d
    #chl_8d

files = os.listdir(data_in) #Liste les fichiers.
files.sort() #Trie les fichiers.
print len(files) #len = longueur de la liste de fichiers.

#b = 2003
#a = 2002
#d2 = {}


for myfile in files:
    
#    day= 185
#    day2= 0

#for a in range (2002,2003):
#    print a
#    while day2 < 235:
#        day2= day+7
#        if day2 > 365:
#            day2 = 365
#        if a % 4 == 0 and day2 == 365:
#            day2 = 366
        
    i =1
    File = SD(data_in+myfile, SDC.READ) #   Lire depuis le hdf.
    l3 = File.select('l3m_data') #  Et met le contenu dans File.
    l3d = l3.get() #    Fonction get() pour avoir vraiment le tableau pour lire le hdf.
    #print 'min/max :', l3d.min(),l3d.max() # On peut demander les valeurs min / max.

    
    while i <= p:

        ymaxZI = int(d['ymax'+str(i)])*43.2964
        yminZI = int(d['ymin'+str(i)])*43.2964
        xmaxZI = int(d['ymax'+str(i)])*43.2964
        xminZI = int(d['ymin'+str(i)])*43.2964

        varnum=3  # on a dl plusieurs variables (ligne 23)
        varg=['sst11mic_8d','poc_8d', 'nsst_8d','chl_8d'][varnum]
        title=[u'Temperature de surface en °C',u'Carbone organique particlaire (POC) en mg.m-3',u'Temperature de surfarce nocturne en °C',u'Chlorophylle en mg.m-3'][varnum]
        FillValue=[65535.0,-32737.0,-32737.0,-32737.0]
        slI=[(0.00071718,-2),(1,0),(0.00071718,-2),(1,0)][varnum] # cette fois varnum récupère pente et intercept. 
        slope=slI[0] # égal au premier de la paire
        intercept=slI[1] 

        ScaledDataMinimum= [-2,10,-2,0.01][varnum] # Nous sert dans la formule de convertion. Scaled = données mises à l'échelle.
        ScaledDataMaximum= [45,1000,45,20][varnum] # Donne les futurs min / max des unités de valeurs.

        vmin=ScaledDataMinimum
        vmax=ScaledDataMaximum

        l3d[ (l3d < vmin) & (l3d != FillValue) ] = vmin #
        l3d[ l3d > 10 ] = 10.0 #
        if l3d.any()<0.011:
            l3d[ l3d == FillValue ] = np.nan #0.011 0.00001 #

        ZIl3d=l3d[yminZI:ymaxZI,xminZI:xmaxZI] # Echantilloner la ZI. Distance lignes puis colonnes.
        ZIl3dR=(ZIl3d*slope)+intercept
        ZIl3dR=np.dot(ZIl3dR,1.0) #   CRUCIAL : transformation en objet numpy pour manipuler plus facilement

        print 'min/max :', l3d.min(),l3d.max()

        filen = data_out+myfile[0:38]+'_ZI'  #'A'+str(a)+str(format(day,'03'))+str(a)+str(format(day2,'03'))+'.'+varg+
        print filen+str(i)
        
        np.array([ZIl3dR])
        numpy.save(filen+str(i), ZIl3dR)
        
        #f = filen+str(i)+'.npy'
        #data = numpy.load(f)
        #data_mean = numpy.mean(data)
        
        #d2['ZI'+str(i)] = data_mean
        
        
        i=i+1                
#    day= day+8
#    if a == 2015 and day2 == 32:
#        day2 = 365
#day= 1
#day2= 0
#    
#b = b+1
#                
#plt.plot(int(d2['ZI1']), int(d2['ZI2']),'o')
#plt.plot(int(d2['ZI2']),'o')
#
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('filen')
#
#plt.show()
                

#np.mean('test.npy')
#
#x,y = numpy.load("test.npy")
#
#plt.plot(x,y,'o')
#
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title("Tracé test")
#
#plt.show()                


print 'Fin'
