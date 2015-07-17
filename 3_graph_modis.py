# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 09:49:45 2015

@author: Pierre-Alain Mannoni, Térence Philippon
"""
# Email : Pierre-Alain.MANNONI@unice.fr & terence.philippon@sfr.fr

# ** Pour MODISA et SWF : Traitement mathématique et save en .npy **
# ** NbTot de data, Moyenne, Ecart-type, mini/max, nb de NAN **
# ** utilisation des fichiers ZI créés préalablement **
#################################################################################
# Plot graphique après le stockage des valeurs recherchées dans une matrice.
# Valable en 8 et 32D (vérifier la concordance des lignes commentées/activées)
# 
# Remarques :
# La mise à l'échelle de l'axe des x en fin de script est modifiable suivant les
# données utilisées (nb de fichiers pour longueur axe) et l'affichage souhaité.
# ===============================================================================
# =========================== Imports ===========================================

import os
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

#--------------------- Définition variables et directory ------------------------

sensor = 'swf'
reso = '9km'

varnum = 3
#variable = ['nsst_8d', 'poc_8d', 'sst11mic_8d', 'chl_8d'][varnum]                   # variables 8D
variable = ['nsst_32d', 'poc_32d', 'sst11mic_32d', 'chl_32d'][varnum]               # variables 32D

data_out = '/home/pressions/SATELITIME/data/graphiques/'
data_in ='/home/pressions/SATELITIME/data/ZI/'+sensor+'/'+variable+'/'+reso+'/'      # Local path
os.chdir(data_in)
files = os.listdir(data_in)                         # Liste les fichiers.
files.sort()                                        # Trie les fichiers.
print len(files)                                    # len = longueur de la liste de fichiers.
f=len(files)                                        # ('Combien de fichiers ? --> ')   #Nb fichiers : Nb lignes.

# -------------------------- Creation matrice vide ------------------------------
ZIs= np.load(files[0])
j=len(ZIs)/2                        # Nombre de ZI (1er element de [ZIs] = coord, 2e element = data)
expr=[]                             # Liste pour former la matrice
for numzi in range(0,j):
    expr=expr+[('zi'+str(numzi)+'n','f8'),('zi'+str(numzi)+'moy','f8'),('zi'+str(numzi)+'et','f8'),('zi'+str(numzi)+'min','f8'),('zi'+str(numzi)+'max','f8'),('zi'+str(numzi)+'nan','f8')]
expr=[('date','i8')]+expr    
print expr
arr = np.zeros((f,),dtype=expr)     # matrice vide à remplir de taille 'expr'
# -------------------------------------------------------------------------------
# ------------------------- Boucle data stockage --------------------------------
i = 0
for myfile in files:
    
    date= int(myfile[1:15])         # Extraction de la date
    ZIs= np.load(myfile)            # Chargement en numpy
    
    n = 0                           # numero de la ZI
    dline=[]                        # --> liste pour stockage successif des lines de données
    while n <= j+2:                 # tant que n 
        print myfile
        coord = ZIs[n]
        data = ZIs[n+1]
        data_num=data.size
        data_mean = np.nanmean(data)
        data_nanmin=np.nanmin(data)
        data_nanmax=np.nanmax(data)
        data_nanstd=np.nanstd(data) 
        data_nan=np.isnan(data).sum()
        dline=dline+[data_num,data_mean,data_nanstd,data_nanmin,data_nanmax,data_nan]
        n=n+2
    dline=[date]+dline      # --> Stockage des lignes de données avec la date
    print dline
    arr[i]=tuple(dline)
    i=i+1

# -------------------- Bornes mois ou saisons  ----------------------------------

i =0
date=[]
mois=['janv','fev','mars','avr','mai','juin','juill','aout','sept','oct','nov','dec']
mois=mois*13                # Pour couvrir 13 années
for myfile in files :       # Boucle : Arrondi de la date au mois. 
    print '..........',myfile
    annee = myfile[1:5]     
    j = myfile[5:8]
    jour=int(j)
    i = int(jour / 30.5)                # Arrondi (interger)
    if i >= 12:                         # 0 = janvier et 11 = décembre
        i = 11

    date=date+[str(mois[int(i)]+'-'+str(annee))]

# ------------------------- Plot graphique --------------------------------------

plt.plot(arr['zi0moy'],color='r', linestyle='-', label='Guadeloupe')        
plt.plot(arr['zi1moy'],color='b', linestyle='-', label='Martinique')        
plt.plot(arr['zi2moy'],color='g', linestyle='-', label='Iles_du_Nord')       
plt.plot(arr['zi3moy'],color='y', linestyle='-', label=u'Témoin(large)')     
#plt.plot(arr['zi1et'], label='Ecart-type')
#plt.axis([0,arr.all['date'],0,1])

plt.title('Graphique pour '+variable+' '+reso+' '+sensor) 
plt.xlabel('Temps')
plt.ylabel('[chlor-a] : mg/m3')
plt.legend()
print 'Guadeloupe, Martinique, Iles de Nord, Large'
print 'zi0,         zi1,        zi2,        zi3'
# ---------- Mise à l'échelle de l'axe des x ---------------
h=[date[u] for u in range(0,size(date),46)]             ### 8D # 'Pas' de 46 pour tomber sur le même mois (~8jours/365)
p=range(0,size(date),46)                                       # ~13 valeurs, de 2002 à 2015.
plt.xticks(p,h, fontsize=9, rotation=90)                # re-échelonnage de l'axe des x
subplots_adjust(bottom=0.15)
# ----------------------------------------------------------
#plt.savefig(data_out+sensor+'_'+reso+'_'+variable+'_Graphique.png')

plt.show()

