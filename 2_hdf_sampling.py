# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:32:07 2015
@author: Pierre-Alain Mannoni, Térence Philippon
"""
# Email : Pierre-Alain.MANNONI@unice.fr & terence.philippon@sfr.fr

#####          ** Affichage ZR et ZIs avant extraction **
#       ** Changer les variables directement et/ou avec varnum **
#################################################################################
# Extraction par zones (ZI / ZR) des données du site oceandata.sci.gsfc.nasa.gov
# ZI : zones d'intérêts, en général de petite taille pour traitement graphique. 
# ZR : zone régionale, de taille plus grande pour générer des .png.
# Remarques :
# La boucle en fin est à activer si l'on veut traiter plusieurs variables en même 
# temps. Les coordonnées des ZR et ZI peuvent être modifiées directement dans le script.  
# ===============================================================================
# ============= Imports =========================================================

import os,sys
from pyhdf.SD import SD, SDC   
#from mpl_toolkits.basemap import Basemap
from pylab import mpl as mpl
import matplotlib.pyplot as plt
import numpy as np
#from matplotlib.patches import Polygon
# =========================================================================
# =========================== Definition Varaibles ========================

bzi=40                                                                  # marge autour des ZI pour le zoom
varnum = 3                                                              # varnum pour 1 seule variable
sensor = 'aqua'                                                          # swf ou aqua
reso = '9km'                                                            # résolution '4km', '4', '9km' ou '9'.
# ---- variables 8D / 32D ------------------------------------------
#variable = ['nsst_8d', 'poc_8d', 'sst11mic_8d', 'chl_8d'][varnum]       # variables 8D
variable = ['nsst_32d', 'poc_32d', 'sst11mic_32d', 'chl_32d'][varnum]   # variables 32D
FillValue=[65535.0,-32767.0,-32767.0,-32767.0]                          # Fill values pour chaque variable
slI=[(0.00071718,-2),(1,0),(0.00071718,-2),(1,0)]                       # Pentes et intercept pour 'nsst_8d', 'poc_8d', 'sst11mic_8d', 'chl_8d'
slope=slI[varnum][0]                                                    # égal au premier de la paire
intercept=slI[varnum][1] 
nzi=4                                                                   # nombre de zi
ezi=np.zeros((nzi,),dtype=('i4,i4,i4,i4'))                              # Stockage des coordonnées des ZI

# Image aqua 4km ou swf 9km ----------------------------------------
imfile = '/home/pressions/SATELITIME/data/Chl2009_9km.hdf'          # Image pour voir les pixels (choisir la bonne résolution)
#imfile = '/home/pressions/SATELITIME/data/AQUA_Chl2009_4km.hdf'        

# Definition de la Zone Regionale : ZR -----------------------------
xzrmin,xzrmax,yzrmin,yzrmax=1250,1750,750,1100                          # ZR pour 9km
#xzrmin,xzrmax,yzrmin,yzrmax=2500,3500,1500,2200                        # ZR pour 4km

# Definition des colormaps -----------------------------------------
norm=mpl.colors.LogNorm(vmin=0.01, vmax=20)
colors = [(0.33,0.33,0.33)] + [(plt.cm.jet(i)) for i in xrange(1,256)]
new_map = mpl.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256) # Colormap
colors = [(0.33,0.33,0.33)] + [(plt.cm.gray(i)) for i in xrange(1,256)]
new_map_gray = mpl.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256) # Colormap

# ---- Sampling Guadeloupe, Martinique, Iles du Nord, Large : xmin, xmax, ymin, ymax -----
ezi[0:nzi]=([(1430,1433,882,888),(1433,1437,901,907),(1410,1412,861,864),(1710,1717,897,902)])          # Coordonnées des ZI 9km (ajustées)
#ezi[0:nzi]=([(2860,2866,1764,1777),(2867,2874,1802,1814),(2820,2825,1722,1728),(3420,3434,1795,1805)])  # Coordonnées des ZI 4km (ajustées)
#ezi[0:nzi]=([(2858,2804,1764,1776),(2870,2876,1804,1814),(2816,2820,1720,1726),(3430,3436,1800,1806)])  # Coordonnées des ZI 4km
# ----------------------------------------------------------------

# ================================= zone régionale ==============================
#                               
fzr = SD(imfile, SDC.READ)      #  Lire depuis le hdf.
data = fzr.select('l3m_data')   #  choisit le hdf datasets
data = data.get()               #  Fonction get() pour avoir vraiment le tableau pour lire le hdf.
#data = np.dot(data,1.0)
zr=data[yzrmin:yzrmax,xzrmin:xzrmax]
plt.imshow(zr,norm=norm,extent=[xzrmin,xzrmax,yzrmin,yzrmax],origin='lower', cmap=new_map,interpolation='none',aspect='equal') #
plt.gca().invert_yaxis()
plt.show()
# -------------------------- Boucle zone d'intérêt --------------------------
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
    
# ================= Test de démarrage ===========================
go=raw_input('Extraire les données ? oui / NON : ')
if go=='oui':
# sys.exit()                                                             ### <-- sys.exit pour tester
    
###################### EXTRACTION  DES DONNEES
#for varnum in [0,1,2,3]:                   ### --> A activer si les 4 variables sont DL --> Indenter la suite 1 fois
                                            # Si une seule variable --> Ne pas indenter davantage

    
    slope=slI[varnum][0]                            #  égal au premier de la paire
    intercept=slI[varnum][1] 
    # ================== définition path =========================
    pathZR ='/home/pressions/SATELITIME/data/ZR/'+sensor+'/'+str(variable)+'/'+reso+'/'
    pathZI ='/home/pressions/SATELITIME/data/ZI/'+sensor+'/'+str(variable)+'/'+reso+'/'                       
    data_in ='/home/pressions/SATELITIME/data/FULL/'+str(variable)+'/'+sensor+'/'+reso+'/'
    print data_in,pathZR,pathZI
    
    
    files = os.listdir(data_in)                     #  Liste les fichiers.
    files.sort()                                    #  Trie les fichiers.
    print len(files)                                #  len = longueur de la liste de fichiers.
    for myfile in files:
        print myfile
        File = SD(data_in+myfile, SDC.READ)         #  Lire depuis le hdf.
        data= File.select('l3m_data')               #  Et met le contenu dans File.
        data = data.get()                   
        zr=data[yzrmin:yzrmax,xzrmin:xzrmax]                
        zr=zr.astype('float')                       # Pour accepter des nan        
        zr[ zr == FillValue[varnum] ] = np.nan        
        zr=(zr*slope)+intercept      
        
        filezi = pathZI+'/'+myfile[0:39]+'_ZIs.npy'
        filezr = pathZR+'/'+myfile[0:39]+'_ZR.npy'
        np.save(filezr,zr)
        
        ZIs=[]
        for i in range(0,nzi):
            xzimin,xzimax,yzimin,yzimax=ezi[i][0],ezi[i][1],ezi[i][2],ezi[i][3]
            zi=data[yzimin:yzimax,xzimin:xzimax]
            zi=zi.astype('float')
            zi[ zi == FillValue[varnum] ] = np.nan        
            zi=(zi*slope)+intercept 
            ZIs=ZIs+[(xzimin,xzimax,yzimin,yzimax),zi]
            
#        sys.exit()                                                     ### <-- sys.exit pour tester
        np.save(filezi,ZIs)                                            ### SAVE

print 'Fin'


