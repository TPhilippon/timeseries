# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 11:55:27 2015

@author: upression1
"""


path = '/home/pressions/SATELITIME/ddata/chl_8d/hdf/'
files = os.listdir(path) #Liste ldes fichiers.
files.sort() #Trie les fichiers.
print len(files) #len = longueur de la liste de fichiers.

myfile = 'A20021852002192.L3m_8D_CHL_chlor_a_4km.bz2.hdf'
File_Name = myfile
File = SD(path+File_Name, SDC.READ) #   Lire depuis le hdf.
l3 = File.select('l3m_data') #  Et met le contenu dans File.
l3d = l3.get() #    Fonction get() pour avoir vraiment le tableau pour lire le hdf.
    
i=1
while i <= p:
    
    print 'min/max :', l3d.min(),l3d.max() # On peut demander les valeurs min / max.
    ymaxZI = int(d['ymax'+str(i)])*43.2964
    yminZI = int(d['ymin'+str(i)])*43.2964
    xmaxZI = int(d["ymax"+str(i)])*43.2964
    xminZI = int(d["ymin"+str(i)])*43.2964
    i=i+1
    
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
    ZIl3dR=np.dot(l3d,1.0) #   CRUCIAL : transformation en objet numpy pour manipuler plus facilement

    print 'min/max :', l3d.min(),l3d.max()
    
    path ='/home/pressions/SATELITIME/Github/sdatats/Graph_data/'
    numpy.save(path+'ZI_'+str(i), ZIl3d)

np.mean('test.npy')

x,y = numpy.load("test.npy")

plt.plot(x,y,'o')

plt.xlabel('x')
plt.ylabel('y')
plt.title("Tracé test")

plt.show()

print 'Fin'