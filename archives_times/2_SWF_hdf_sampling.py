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
bzi=20  # marge autour des ZI pour la zoom
xzrmin,xzrmax,yzrmin,yzrmax=1250,1750,750,1100      # Coordonnées SWF
# 2500,3500,1500,2200                               # Coordonnées MODIS

nzi=4   # nombre de zi
ezi=np.zeros((nzi,),dtype=('i4,i4,i4,i4'))          # Stockage des coordonnées des ZI
ezi[0:nzi]=([( 1429 ,  1432 ,   882 ,   888 ),
       ( 1435 ,  1438 ,   902 ,   907 ),
       ( 1408 ,  1410 ,   860,   863),
       ( 1715 ,  1718 ,   900 ,   903)])            # Coordonnées des ZI SWF
#ezi[0:nzi]=([(2862,2868,1766,1774),(2870,2874,1810,1814),(2858,2862,1741,1745),(3430,3434,1800,1805)])  # Coordonnées des ZI MODIS

pathZR ='/home/pressions/SATELITIME/data/ZR/swf/' 
pathZI ='/home/pressions/SATELITIME/data/ZI/swf/'                            #  Unix
data_in ='/home/pressions/SATELITIME/data/FULL/'+str(variable)+'/swf/'
imfile = '/home/pressions/SATELITIME/data/SWF_Chl2009_9km.hdf' 

FillValue=[65535.0,-32767.0,-32767.0,-32767.0]            #  Pour valeurs NAN.
slI=[(0.00071718,-2),(1,0),(0.00071718,-2),(1,0)][varnum] #  varnum récupère pente et intercept. 
slope=slI[0]                                              #  égal au premier de la paire.
intercept=slI[1] 

norm=mpl.colors.LogNorm(vmin=0.01, vmax=20)
colors = [(0.33,0.33,0.33)] + [(plt.cm.jet(i)) for i in xrange(1,256)]
new_map = mpl.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256) # Colormap
colors = [(0.33,0.33,0.33)] + [(plt.cm.gray(i)) for i in xrange(1,256)]
new_map_gray = mpl.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256) # Colormap
# ==============================================================================

# ------------------------------ zone régionale --------------------------------
fzr = SD(imfile, SDC.READ)      #  Lire depuis le hdf.
data = fzr.select('l3m_data')   #  Et met le contenu dans File.
data = data.get()               #  Fonction get() pour avoir vraiment le tableau pour lire le hdf.
#data = np.dot(data,1.0)
zr=data[yzrmin:yzrmax,xzrmin:xzrmax]
plt.imshow(zr,norm=norm,extent=[xzrmin,xzrmax,yzrmin,yzrmax],origin='lower', cmap=new_map,interpolation='none',aspect='equal') #
plt.gca().invert_yaxis()
plt.show()
    #------------ zone(s) d'intérêt -------------
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
    
######################
files = os.listdir(data_in) #  Liste les fichiers.
files.sort()                #  Trie les fichiers.
print len(files)            #  len = longueur de la liste de fichiers.
for myfile in files:
    print myfile
    File = SD(data_in+myfile, SDC.READ) #  Lire depuis le hdf.
    data= File.select('l3m_data')       #  Et met le contenu dans File.
    data = data.get()                   #  Fonction get() pour avoir vraiment le tableau pour lire le hdf.
    data=(data*slope)+intercept
    data[ data == FillValue[varnum] ] = np.nan 
    zr=data[yzrmin:yzrmax,xzrmin:xzrmax]
    filezi = pathZI+myfile[0:38]+'_ZIs_swf.npy'
    filezr = pathZR+myfile[0:38]+'_ZR_swf.npy'
    np.save(filezr,data)
    
    ZIs=[]
    for i in range(0,nzi):
        print i
        xzimin,xzimax,yzimin,yzimax=ezi[i][0],ezi[i][1],ezi[i][2],ezi[i][3]
        zi=data[yzimin:yzimax,xzimin:xzimax]
        ZIs=ZIs+[(xzimin,xzimax,yzimin,yzimax),zi]
        
    np.save(filezi,ZIs)

print 'Fin'


