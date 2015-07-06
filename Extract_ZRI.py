# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:32:07 2015

@author: Terence, Pierre-Alain, UMR
"""


import os
import Image
import sys
from pyhdf.SD import SD, SDC   
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
import numpy

# =========================== Definition Varaibles =======================
varnum = 3
variable = ['nsst_8d', 'pic_8d', 'sst11mic_8d', 'chl_8d'][varnum]
border=0.5 # marge autour des ZI pour la zoom

#data_out ='Y:\\home\\pressions\\SATELITIME\\sdatats\\Graph_data\\'   #Win
#data_in ='Y:\\SATELITIME\\ddata\\'+str(variable)+'\\hdf'

data_out1 ='/home/pressions/SATELITIME/sdatats/Graph_data/ZR/' 
data_out2 ='/home/pressions/SATELITIME/sdatats/Graph_data/ZI/'  #Unix
data_in ='/home/pressions/SATELITIME/ddata/'+str(variable)+'/hdf/'
# ========================================================================
def draw_screen_poly2( lats2, lons2, m):
    x, y = m( lons2, lats2 )
    xy = zip(x,y)
    poly = Polygon( xy, edgecolor='black', fill=False, alpha=1.5 )
    plt.gca().add_patch(poly)

#---------------------------- Choix de la zone régionale -------------------------

print "Choix de la zone régionale, patienez..."
#m = Basemap(projection='cyl',resolution='c')
#m.drawlsmask(land_color='black',ocean_color='None',lakes=True)
img = '/home/pressions/SATELITIME/sdatats/Graph_data/V20120012012366.L3m_YR_NPP_CHL_chlor_a_4km.nc.png'
#im=Image.open(img)
x=0
y=0
#im = plt.imshow(im,extent=(x-180,x+180,y+90,y-90), interpolation='none')
#
#plt.show()

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
ymax =90# 30
ymin =89.5#-7
xmax = -179#-33
xmin = -180#-100
# -------------------------------------------------------------------------------
#--------------------- Choix d'une/des zone(s) d'intérêt ------------------------
print ("Choix des zones d'intérêt (ZI). Patientez...")

m = Basemap(projection='cyl',llcrnrlat=ymin, urcrnrlat=ymax, llcrnrlon=xmin, urcrnrlon=xmax,resolution='c')
m.drawlsmask(land_color='black',ocean_color='None',lakes=True)
im=Image.open(img)
im2 = plt.imshow(im,extent=(x-180,x+180,y+90,y-90), interpolation='none')
plt.show()

j =raw_input('Combien de ZI à délimiter?: ')
j = int(j)

p = j       #nombre de ZI gardée en mémoire
i = 0       #compteur des ZI pour déroulement boucle
n = 1       #Compteur pour les max/min coordonnées
d ={}
latmin = 9999
latmax = -9999
longmin = 9999
longmax = -9999

while i < j: # Selection des ZI
    print "ZI restantes:"
    print j
    print "Entrez vos coordonnées:"
    
    urcrnrlat = 14.75
    llcrnrlat =14.60 
    urcrnrlon =-60.65 
    llcrnrlon =-60.80
    
#    urcrnrlat =float(raw_input('ymax : '))
#    llcrnrlat =float(raw_input('ymin : '))
#    urcrnrlon =float(raw_input('xmax : '))
#    llcrnrlon =float(raw_input('xmin : '))
    
    choix =raw_input('Valider o/n?: ')
    
    if choix =="o": 
   # ========== trouver lesbornes de l'ensemble des ZI pour un zoom =============
        
        latmin=min(latmin,llcrnrlat)
        latmax=max(latmax,urcrnrlat)   
        longmin=min(longmin,llcrnrlon)
        longmax=max(longmax,urcrnrlon)
   # ============================================================================
           
#        
#        if (float(llcrnrlat)) <= latmin:
#            latmin = llcrnrlat
#        if (float(urcrnrlat)) >= latmax:
#            latmax = urcrnrlat
#        if (float(llcrnrlon)) <= longmin:
#            longmin = llcrnrlon
#        if (float(urcrnrlon)) >= longmax:
#            longmax = urcrnrlon_test
        
        print "Coordonnées validées."
        j = j - 1
     
     # =====Arrondi pour ajuster le cadre au pixel près ================
        
        urcrnrlat = round((90-(urcrnrlat))/0.04166666)   # Conversion en pixel
        llcrnrlat = round((90-(llcrnrlat))/0.04166666)
        urcrnrlon = round(((urcrnrlon)+180)/0.04166666)
        llcrnrlon = round(((llcrnrlon)+180)/0.04166666)
        
#        urcrnrlat = round(float(urcrnrlat)/0.08333333)
#        llcrnrlat = round(float(llcrnrlat)/0.08333333)
#        urcrnrlon = round(float(urcrnrlon)/0.08333333)
#        llcrnrlon = round(float(llcrnrlon)/0.08333333)
        print urcrnrlat
        
        d['ymax'+str(n)] = (90-((urcrnrlat)*0.04166666)) # Stockage en degré corrigé
        d['ymin'+str(n)] = (90-((llcrnrlat)*0.04166666))
        d['xmax'+str(n)] = ((urcrnrlon)*0.04166666)-180
        d['xmin'+str(n)] = ((llcrnrlon)*0.04166666)-180
        
#        d['ymax'+str(n)] = urcrnrlat*0.08333333
#        d['ymin'+str(n)] = llcrnrlat*0.08333333
#        d['xmax'+str(n)] = urcrnrlon*0.08333333
#        d['xmin'+str(n)] = llcrnrlon*0.08333333
        # ==============================================================
        
        # Cadre de la ZI
        lats2 = [ d["ymin"+str(n)], d["ymax"+str(n)], d["ymax"+str(n)], d["ymin"+str(n)] ]
        lons2 = [ d["xmin"+str(n)], d["xmin"+str(n)], d["xmax"+str(n)], d["xmax"+str(n)] ]
        
        print lats2,lons2
        draw_screen_poly2( lats2, lons2, m )  # Dessin des cadres des ZI
        n = n + 1
        
    else:
        print "recommencez."
        
print "Chargement..."

latminr = (float(latmin)-border)              # Encadrement de l'ensemble des ZI
latmaxr = (float(latmax)+border)
longminr = (float(longmin)-border)
longmaxr = (float(longmax)+border)

lats = [ latminr, latmaxr, latmaxr, latminr ]
lons = [ longminr, longminr, longmaxr, longmaxr ]

print 'x,y',x,y
m = Basemap(projection='cyl',llcrnrlat=latminr, urcrnrlat=latmaxr, llcrnrlon=longminr, urcrnrlon=longmaxr,resolution='c')
m.drawlsmask(land_color='black',ocean_color='None',lakes=True)
im=Image.open(img)
im = plt.imshow(im,extent=(x-179.9792,x+179.9792,y+90,y-90), interpolation='none')
        
#def draw_screen_poly( lats, lons, m):   #(ancien Rectangle ZR)
#    x, y = m( lons, lats )
#    xy = zip(x,y)
#    poly = Polygon( xy, edgecolor='Red', fill=False, alpha=1.5 )
#    plt.gca().add_patch(poly)
#
#draw_screen_poly( lats, lons, m )
    
plt.show()

#sys.exit()
#----------------------------------------------------------------------------
#--------------------- Lecture hdf et Extraction (save) ---------------------

    #==================== Extraction ZR ==================================

print data_in
    #nsst_8d  
    #pic_8d
    #sst11mic_8d
    #chl_8d

files = os.listdir(data_in) # Liste les fichiers.
files.sort()                # Trie les fichiers.
print len(files)            # len = longueur de la liste de fichiers.


for myfile in files:        # Boucle sur les fichiers.
    
    print myfile
    i =1
    File = SD(data_in+myfile, SDC.READ)     #    Lire depuis le hdf.
    l3 = File.select('l3m_data')            #    Et met le contenu dans File.
    l3d = l3.get()                          #    Fonction get() pour avoir vraiment le tableau pour lire le hdf.
    #print 'min/max :', l3d.min(),l3d.max() #    On peut demander les valeurs min / max.
    l3d = np.dot(l3d,1.0)

#    xminZR,xmaxZR=np.sort([abs(float(xmin)*43.2964),abs(float(xmax)*43.2964)])
#    yminZR,ymaxZR=np.sort([abs(float(ymin)*43.2964),abs(float(ymax)*43.2964)])
    
    xminZR,xmaxZR=np.sort([abs(float(xmin+179.9792)/0.0416666),abs(float(xmax+179.9792)/0.0416666)])
    yminZR,ymaxZR=np.sort([abs(float(-ymin+90)/0.0416666),abs(float(-ymax+90)/0.0416666)])

#    xminZR,xmaxZR=np.sort([abs(float(xmin)/0.08333333),abs(float(xmax)/0.08333333)])
#    yminZR,ymaxZR=np.sort([abs(float(ymin)/0.08333333),abs(float(ymax)/0.08333333)])
    
    print "xminZR,xmaxZR",xminZR,xmaxZR
    print "yminZR,ymaxZR",yminZR,ymaxZR
    varg=['sst11mic_8d','poc_8d', 'nsst_8d','chl_8d'][varnum]
    title=[u'Temperature de surface en °C',u'Carbone organique particlaire (POC) en mg.m-3',u'Temperature de surfarce nocturne en °C',u'Chlorophylle en mg.m-3'][varnum]
    FillValue=[65535.0,-32767.0,-32767.0,-32767.0]
    slI=[(0.00071718,-2),(1,0),(0.00071718,-2),(1,0)][varnum] #varnum récupère pente et intercept. 
    slope=slI[0]                                              # égal au premier de la paire
    intercept=slI[1] 

#    ScaledDataMinimum= [-2,10,-2,0.01][varnum]     # Sert dans la formule de convertion. Scaled = données mises à l'échelle.
#    ScaledDataMaximum= [45,1000,45,20][varnum]     # Donne les futurs min / max des unités de valeurs.

    ZRl3d=l3d[yminZR:ymaxZR,xminZR:xmaxZR] # Echantilloner la ZR. Distance lignes puis colonnes.
    ZRl3dR=(ZRl3d*slope)+intercept
    
    print "ZRl3d",ZRl3d
    print "ZRl3dR",ZRl3dR

    ZRl3dR[ ZRl3dR == FillValue[varnum] ] = np.nan  # Annulation des valeurs extrêmes

    filen = data_out1+myfile[0:38]+'_ZR'            # Nom du fichier sauvegardé.
    print filen

    w = ZRl3dR.shape
    print(w)
    numpy.save(filen, ZRl3dR)
    # =======================================================================
    # ====================== Extraction ZI ==================================
    
    ZIs=[]              # Liste pour sauvegarder plus de données après.
    while i <= p:       # Boucle sur les ZI.
        
        xminZI,xmaxZI=np.sort([abs(round((float(d['xmin'+str(i)])+179.9792)/0.0416666)),abs(round((float(d['xmax'+str(i)])+179.9792)/0.0416666))])
        yminZI,ymaxZI=np.sort([abs(round((float(90-d['ymin'+str(i)]))/0.0416666)),abs(round((float(90-d['ymax'+str(i)]))/0.0416666))])

#        xminZI,xmaxZI=np.sort([abs(round((float(d['xmin'+str(i)])+180)/0.0833333)),abs(round((float(d['xmax'+str(i)])+180)/0.0833333))])
#        yminZI,ymaxZI=np.sort([abs(round((float(90-d['ymin'+str(i)]))/0.0833333)),abs(round((float(90-d['ymax'+str(i)]))/0.0833333))])
#        ymaxZI = abs(int(d['ymax'+str(i)])*43.2964)
#        yminZI = abs(int(d['ymin'+str(i)])*43.2964)
#        xmaxZI = abs(int(d['xmax'+str(i)])*43.2964)
#        xminZI = abs(int(d['xmin'+str(i)])*43.2964)

        print xminZI, xmaxZI
        print yminZI, ymaxZI

        ZIl3d=l3d[yminZI:ymaxZI,xminZI:xmaxZI]          # Echantilloner la ZI. Distance lignes puis colonnes.
        ZIl3dR=(ZIl3d*slope)+intercept                  # Scaling equation (parameter value).  
        ZIl3dR[ ZIl3dR == FillValue[varnum] ] = np.nan  # Annulation des valeurs extrêmes.
        
        print "nombre de pixels : ", ZIl3d.size, np.prod(ZIl3d.shape)
        #ZIl3dR = np.array([ZIl3dR])
#        l[s] = ZIl3dR  
#        s=s+1   
        
        #numpy.save(filen+str(i), ZIl3dR)
        ZIs=ZIs+[(yminZI,ymaxZI,xminZI,xmaxZI,d['ymin'+str(i)],d['ymax'+str(i)],d['xmin'+str(i)],d['xmax'+str(i)]),ZIl3dR]
        i=i+1                
        raw_input()
    #numpy.savez(filen, l)
    filen = data_out2+myfile[0:38]+'_ZI'  #'A'+str(a)+str(format(day,'03'))+str(a)+str(format(day2,'03'))+'.'+varg+
    print filen
    numpy.save(filen, ZIs)
    # ===============================================================

print 'Fin'


