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


bzi=40  # marge autour des ZI pour la zoom
# Definition de la Zone Regionale : ZR =======================
xzrmin,xzrmax,yzrmin,yzrmax=2500,3500,1500,2200
# Definition des colormaps
norm=mpl.colors.LogNorm(vmin=0.01, vmax=20)
colors = [(0.33,0.33,0.33)] + [(plt.cm.jet(i)) for i in xrange(1,256)]
new_map = mpl.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256) # Colormap
colors = [(0.33,0.33,0.33)] + [(plt.cm.gray(i)) for i in xrange(1,256)]
new_map_gray = mpl.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256) # Colormap

FillValue=[65535.0,-32767.0,-32767.0,-32767.0] # Fill values pour chaque variable
slI=[(0.00071718,-2),(1,0),(0.00071718,-2),(1,0)] #Parametres de pentes et intercept pour chaque variable 'nsst_8d', 'poc_8d', 'sst11mic_8d', 'chl_8d'

nzi=4   # nombre de zi
ezi=np.zeros((nzi,),dtype=('i4,i4,i4,i4'))   #  Stockage des coordonnées des ZI
# Sampling Guadeloupe, Martinique, Iles du Nord, Large : xmin, xmax, ymin, ymax
ezi[0:nzi]=([(2860,2866,1764,1777),(2867,2874,1802,1814),(2820,2825,1722,1728),(3420,3434,1795,1805)])  # Coordonnées des ZI



varnum = 3
variable = ['nsst_8d', 'poc_8d', 'sst11mic_8d', 'chl_8d'][varnum]


imfile = '/home/pressions/SATELITIME/data/AQUA_Chl2009_4km.hdf' 

#  varnum récupère pente et intercept. 
slope=slI[varnum][0]                                              #  égal au premier de la paire
intercept=slI[varnum][1] 
# ==============================================================================
#                               zone régionale
fzr = SD(imfile, SDC.READ)      #  Lire depuis le hdf.
data = fzr.select('l3m_data')   #  choisit le hdf datasets
data = data.get()               #  Fonction get() pour avoir vraiment le tableau pour lire le hdf.
#data = np.dot(data,1.0)
zr=data[yzrmin:yzrmax,xzrmin:xzrmax]
plt.imshow(zr,norm=norm,extent=[xzrmin,xzrmax,yzrmin,yzrmax],origin='lower', cmap=new_map,interpolation='none',aspect='equal') #
plt.gca().invert_yaxis()
plt.show()
    #------------ zone d'intérêt
for i in range(0,ezi.size):
    print "ZI numero :",i
    xzimin,xzimax,yzimin,yzimax=ezi[i][0],ezi[i][1],ezi[i][2],ezi[i][3]
    zib=data[yzimin-bzi:yzimax+bzi,xzimin-bzi:xzimax+bzi]
    zi=data[yzimin:yzimax,xzimin:xzimax]
    plt.imshow(zib,norm=norm,extent=[xzimin-bzi,xzimax+bzi,yzimin-bzi,yzimax+bzi],origin='lower', cmap=new_map_gray,interpolation='none',aspect='equal') #
    plt.imshow(zi,norm=norm,extent=[xzimin,xzimax,yzimin,yzimax],origin='lower', cmap=new_map,interpolation='none',aspect='equal') 
    plt.gca().invert_yaxis()
    plt.autoscale()
    plt.show()
    
go=raw_input('Extraire les données ? oui / NON : ')
if go<>'oui':
    sys.exit()
    
###################### EXTRACTION  DES DONNEES



for varnum in [0,1,2,3]:
    
    variable = ['nsst_8d', 'poc_8d', 'sst11mic_8d', 'chl_8d'][varnum]
    slope=slI[varnum][0]                                              #  égal au premier de la paire
    intercept=slI[varnum][1] 
    pathZR ='/home/pressions/SATELITIME/data/ZR/aqua/'+str(variable)
    pathZI ='/home/pressions/SATELITIME/data/ZI/aqua/'+str(variable)                       #  Unix
    data_in ='/home/pressions/SATELITIME/data/FULL/'+str(variable)+'/aqua/hdf/'
    print data_in,pathZR,pathZI
    
    
    files = os.listdir(data_in) #  Liste les fichiers.
    files.sort()                #  Trie les fichiers.
    print len(files)            #  len = longueur de la liste de fichiers.
    for myfile in files:
        print myfile
        File = SD(data_in+myfile, SDC.READ) #  Lire depuis le hdf.
        data= File.select('l3m_data')       #  Et met le contenu dans File.
        data = data.get()                   
        zr=data[yzrmin:yzrmax,xzrmin:xzrmax]                
        zr=zr.astype('float') # Pour accepter des nan        
        zr[ zr == FillValue[varnum] ] = np.nan        
        zr=(zr*slope)+intercept      
        
        filezi = pathZI+'/'+myfile[0:38]+'_ZIs.npy'
        filezr = pathZR+'/'+myfile[0:38]+'_ZR.npy'
        np.save(filezr,zr)
        
        ZIs=[]
        for i in range(0,nzi):
            xzimin,xzimax,yzimin,yzimax=ezi[i][0],ezi[i][1],ezi[i][2],ezi[i][3]
            zi=data[yzimin:yzimax,xzimin:xzimax]
            zi=zi.astype('float')
            zi[ zi == FillValue[varnum] ] = np.nan        
            zi=(zi*slope)+intercept 
            ZIs=ZIs+[(xzimin,xzimax,yzimin,yzimax),zi]
            
        np.save(filezi,ZIs)

print 'Fin'


