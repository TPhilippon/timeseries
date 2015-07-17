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
# temps. Les coordonnées des ZR et ZI peuvent être modifiées dans le script.  
# ===============================================================================
# ============= Imports =========================================================

import os,sys
from pyhdf.SD import SD, SDC   
from pylab import mpl as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal

# =========================================================================
# =========================== Variables parametrables ========================
# =========================================================================
interpolation='yes'
bzi=40    # Buffer autour de la zi pour l'affichage                                                              # marge autour des ZI pour le zoom
varnum = 0                                                              # varnum pour 1 seule variable
sensor = 'aqua'  # 'swf'                                                        # swf ou aqua
reso = '4km'  # '4km' ou '9km'                                                          # résolution '4km', '4', '9km' ou '9'.
listvariable = ['nsst_8d', 'poc_8d', 'sst11mic_8d', 'chl_8d']      # variables 8D
#listvariable = ['nsst_32d', 'poc_32d', 'sst11mic_32d', 'chl_32d']   #[varnum variables 32D

# =========================================================================
# =========================== Definition Varaibles ========================
# =========================================================================

scaling=[[-2,45,'linear'],[10,1000,'log'],[-2,45,'linear'],[0.01,20,'log']]
FillValue=[65535.0,-32767.0,-32767.0,-32767.0]                          # Fill values pour chaque variable
slI=[(0.00071718,-2),(1,0),(0.00071718,-2),(1,0)]                       # Pentes et intercept pour 'nsst_8d', 'poc_8d', 'sst11mic_8d', 'chl_8d'
variable = listvariable[varnum]
slope=slI[varnum][0]                                                    # égal au premier de la paire
intercept=slI[varnum][1] 
vmin=scaling[varnum][0]
vmax=scaling[varnum][1]
scalingtype=scaling[varnum][2]
nzi=4                                                                   # nombre de zi
ezi=np.zeros((nzi,),dtype=('i4,i4,i4,i4'))                              # Stockage des coordonnées des ZI
imfile = '/home/pressions/SATELITIME/data/Chl2009_'+reso+'.hdf'          # Image pour voir les pixels (choisir la bonne résolution)
mois=['janv','fev','mars','avr','mai','juin','juill','aout','sept','oct','nov','dec']
mois=mois*20                # Pour couvrir 13 années
        
# =========================================================================
# Definition de la Zone Regionale : ZR et des zones d'interets -----------------------------
# ---- Sampling Guadeloupe, Martinique, Iles du Nord, Large : xmin, xmax, ymin, ymax -----
# =========================================================================

if reso=='9km':
    xzrmin,xzrmax,yzrmin,yzrmax=1250,1750,750,1100   # Caraibes 
    ezi[0:nzi]=([(1430,1433,882,888),(1433,1437,901,907),(1410,1412,861,864),(1710,1717,897,902)])          # Coordonnées des ZI 9km (ajustées)
if reso=='4km':
    xzrmin,xzrmax,yzrmin,yzrmax=2500,3500,1500,2200
    ezi[0:nzi]=([(2860,2866,1764,1777),(2867,2874,1802,1814),(2820,2825,1722,1728),(3420,3434,1795,1805)])  # Coordonnées des ZI 4km (ajustées)

# Colormap Chl de ref
norm_chl=mpl.colors.LogNorm(vmin=0.01, vmax=20)
colors = [(0.33,0.33,0.33)] + [(plt.cm.jet(i)) for i in xrange(1,256)]
new_map_chl = mpl.colors.LinearSegmentedColormap.from_list('new_map_chl', colors, N=256) 
colors = [(0.33,0.33,0.33)] + [(plt.cm.gray(i)) for i in xrange(1,256)]
new_map_gray_chl = mpl.colors.LinearSegmentedColormap.from_list('new_map_gray_chl', colors, N=256) 

# Colormap Couleur et grise
if scalingtype=='log':norm=mpl.colors.LogNorm(vmin=vmin, vmax=vmax)
if scalingtype=='linear':norm=mpl.colors.Normalize(vmin=vmin, vmax=vmax)
colors = [(0.33,0.33,0.33)] + [(plt.cm.jet(i)) for i in xrange(1,256)]
new_map = mpl.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256) 
colors = [(0.33,0.33,0.33)] + [(plt.cm.gray(i)) for i in xrange(1,256)]
new_map_gray = mpl.colors.LinearSegmentedColormap.from_list('new_map_gray', colors, N=256) 


# =======================================================================
# ======================== zone régionale de reference ==============================
# =======================================================================

# LA ZR est affiché en utilisant un image annuelle de la Chl
                          
fzr = SD(imfile, SDC.READ)      #  Lire depuis le hdf.
l3m = fzr.select('l3m_data')   #  choisit le hdf datasets
l3m = l3m.get()               #  Fonction get() pour avoir vraiment le tableau pour lire le hdf.
#l3m = np.dot(l3m,1.0)
zrref=l3m[yzrmin:yzrmax,xzrmin:xzrmax]
plt.imshow(zrref,norm=norm_chl,extent=[xzrmin,xzrmax,yzrmin,yzrmax],origin='lower', cmap=new_map_chl,interpolation='none',aspect='equal') #
plt.gca().invert_yaxis()
#plt.show()


# =======================================================================
# =========================== zone interet ==============================
# =======================================================================

for i in range(0,ezi.size):
    print "ZI numero :",i
    xzimin,xzimax,yzimin,yzimax=ezi[i][0],ezi[i][1],ezi[i][2],ezi[i][3]
    zib=l3m[yzimin-bzi:yzimax+bzi,xzimin-bzi:xzimax+bzi]
    zi=l3m[yzimin:yzimax,xzimin:xzimax]
    plt.imshow(zib,norm=norm_chl,extent=[xzimin-bzi,xzimax+bzi,yzimin-bzi,yzimax+bzi],origin='lower', cmap=new_map_gray_chl,interpolation='none',aspect='equal') #
    plt.imshow(zi,norm=norm_chl,extent=[xzimin,xzimax,yzimin,yzimax],origin='lower', cmap=new_map_chl,interpolation='none',aspect='equal') 
    plt.gca().invert_yaxis()
    plt.autoscale()
    #plt.show()

bakmap=zrref
bakmap[ bakmap != -32767.] = 0
bakmap[ bakmap == -32767.] = np.nan

# =======================================================================
# ====================EXTRACTION DES DONNEES==============================
# =======================================================================

fig=plt.figure()
ax=fig.add_subplot(111)
plt.ion()
plt.show()
  
pathZR ='/home/pressions/SATELITIME/data/ZR/'+sensor+'/'+str(variable)+'/'+reso+'/'
pathZI ='/home/pressions/SATELITIME/data/ZI/'+sensor+'/'+str(variable)+'/'+reso+'/'                       
data_in ='/home/pressions/SATELITIME/data/FULL/'+str(variable)+'/'+sensor+'/'+reso+'/'
print data_in

files = os.listdir(data_in)                     #  Liste les fichiers.
files.sort()                                    #  Trie les fichiers.
print 'nombre de fichiers',len(files)                                #  len = longueur de la liste de fichiers.
counter=0    
for myfile in files:
    
    print myfile
    date=myfile[1:15]
    annee = myfile[1:5]
    j = int(myfile[5:8])
    j=int(j)
    if j >= 355 or j < 83:
        saison = u'Hiver'
    if j >= 83 and j < 176:
        saison = u'Printemps'
    if j >= 176 and j < 261:
        saison = u'Eté'
    if j >= 261 and j < 355:
        saison = u'Automne'    
    i = int(j / 30.5)                # Arrondi (interger)
    if i >= 12:                         # 0 = janvier et 11 = décembre
        i = 11
    title=saison+'-'+str(mois[int(i)])+'-'+str(annee)
    print myfile,date
    
    
    
    File = SD(data_in+myfile, SDC.READ)         #  Lire depuis le hdf.
    data= File.select('l3m_data')               #  Et met le contenu dans File.
    data = data.get()
    data = data.astype('float') 
    data[ data == FillValue[varnum] ] = np.nan
    data=(data*slope)+intercept       
    zr=data[yzrmin:yzrmax,xzrmin:xzrmax]

    #------------ Interpolation
    zr4i = zr
    if interpolation == 'yes':
        # a boolean array of (width, height) which False where there are missing values and True where there are valid (non-missing) values
        mask = np.isnan(zr)
        mymask=mask    
        mask=~mask
        # array of (number of points, 2) containing the x,y coordinates of the valid values only
        xx, yy = np.meshgrid(np.arange(zr.shape[1]), np.arange(zr.shape[0]))
        xym = np.vstack( (np.ravel(xx[mask]), np.ravel(yy[mask])) ).T
        # the valid values in the first, second, third color channel,  as 1D arrays (in the same order as their coordinates in xym)
        zr = np.ravel( zr[mask] )
        # three separate interpolators for the separate color channels
        interp0 = scipy.interpolate.NearestNDInterpolator( xym, zr )
        # interpolate the whole image, one color channel at a time    
        result0 = interp0(np.ravel(xx), np.ravel(yy)).reshape( xx.shape )
        zr=result0
        zr = zr+bakmap # Masque continent     
    
    filezi = pathZI+'/'+myfile[0:39]+'_ZIs.npy'
    filezr = pathZR+'/'+myfile[0:39]+'_ZR.npy'
    
    #np.save(filezr,zr)
    print 'fillvalue=',FillValue[varnum] ,np.nanmin(zr),np.nanmax(zr)
    plt.title(title+' \n '+myfile)    
    plt.imshow(zr,norm=norm, origin='upper', cmap=new_map)

    if counter == 0 : plt.colorbar()
    counter=counter+1        
    plt.pause(0.0001)
    #sys.exit()
    
    ZIs=[]
    for i in range(0,nzi):
        xzimin,xzimax,yzimin,yzimax=ezi[i][0],ezi[i][1],ezi[i][2],ezi[i][3]
        zi=data[yzimin:yzimax,xzimin:xzimax]
        ZIs=ZIs+[(xzimin,xzimax,yzimin,yzimax),zi]
        
#        sys.exit()                                                     ### <-- sys.exit pour tester
    #np.save(filezi,ZIs)                                            ### SAVE
    plt.imshow(np.zeros(np.shape(zr)),cmap=plt.get_cmap('Greys'))
    plt.cla()
print 'Fin'


