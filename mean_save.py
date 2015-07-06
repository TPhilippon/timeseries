# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 09:49:45 2015

@author: upression1
"""

import os
import numpy as np
from numpy import *
import matplotlib.pyplot as plt

         #------------ Traitement mathématique (moyenne) et sauvegarde en .npy

data_in ='/home/pressions/SATELITIME/sdatats/Graph_data/ZI/'
os.chdir(data_in)
files = os.listdir(data_in) #Liste les fichiers.
files.sort() #Trie les fichiers.
print len(files) #len = longueur de la liste de fichiers.
f=len(files)   #('Combien de fichiers ? --> ')   #Nb fichiers : Nb lignes.



# -------------------------- Creation matrice vide----------------------------------
ZIs= np.load(files[0])
j=len(ZIs)/2 # Nombre de ZI (1er element de la liste = coord, 2e element = data)
expr=[]
for numzi in range(1,j+1):
    expr=expr+[('zi'+str(numzi)+'n','f8'),('zi'+str(numzi)+'moy','f8'),('zi'+str(numzi)+'et','f8'),('zi'+str(numzi)+'min','f8'),('zi'+str(numzi)+'max','f8'),('zi'+str(numzi)+'nan','f8')]
expr=[('date','i8')]+expr    
print expr
arr = np.zeros((f,),dtype=expr)
# ------------------------- Fin creation matrice ----------------------------------

# ------------------------- Boucle data stockage -----------------------------------
i = 0
for myfile in files:
    
    date= int(myfile[1:15])
    ZIs= np.load(myfile)
    
    n = 0  
    dline=[]
    while n <= j: # boucle sur les ZI
        
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
    dline=[date]+dline
    print dline
    arr[i]=tuple(dline)
    i=i+1

# ------------------------- Plot graphique -----------------------------------

plt.plot(arr['zi1moy'], label='Moyenne')
plt.plot(arr['zi1et'], label='Ecart-type')

#plt.axis([0,arr.all['date'],0,1])
#plt.title('Valeurs moyennes de concentration en chlorophylle-a') 
plt.xlabel('Temps')
plt.ylabel('[chlor-a] : mg/m3')


    # -------------------- Bornes mois ou saisons  ------------------------------
f=[4]
ff=[1]
x=10
y=1
i =0
date=[]
mois=['janv','fev','mars','avr','mai','juin','juill','aout','sept','oct','nov','dec']
mois=mois*13
check = 0
for myfile in files :
    x =x+2
    f=f+[x]    
    y=y+1
    ff=ff+[y]
    
    print myfile
    annee = myfile[1:5]     
    j = myfile[5:8]
    
    jour=int(j)
    i = int(jour / 30)
    if i < 1:
        i = 1
    if i > 12:
        i = 12

    date=date+[str(mois[int(i)]+'-'+str(annee))]


h=[date[u] for u in range(0,size(date),46)]     # Pas de 46 pour tomber sur le même mois (~8jours/365)
p=range(0,578,46)                               # 13 valeurs, de 2002 à 2014.
a = plt.plot(ff, f)
   
plt.xticks(p,h)
plt.show()

