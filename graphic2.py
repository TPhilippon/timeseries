# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:15:56 2015

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




         #------------ Graphique

data_in ='/home/pressions/SATELITIME/sdatats/Graph_data/'


#files = os.listdir(data_in) #Liste les fichiers.
#files.sort() #Trie les fichiers.
#print len(files) #len = longueur de la liste de fichiers.


i = 1       #ZI concernée(s). Inclure nouvelle boucle pour x courbe sur 1 graphe.
key = 1      
d={}

print "début boucle"

day= 185
day2= 0
temps = 1

for a in range (2002,2003):
    print a
    while day2 < 365:
        day2= day+7
        if day2 > 365:
            day2 = 365
        if a % 4 == 0 and day2 == 365:
            day2 = 366

        filen = data_in+'A'+str(a)+str(format(day,'03'))+str(a)+str(format(day2,'03'))+'.L3m_8D_CHL_chlor_a_4km_ZI'
        myfile = filen+str(i)+'_mean.npy'
        print myfile
        
        data = numpy.load(myfile)
        print data            
        plt.plot(temps, data, 'g^') # linestyle='--'
        
        d[str(key)] = [str(temps), str(data)]
        key = key +1

        temps = temps +1
        day= day+8
    if a == 2015 and day2 == 32:
        day2 = 365
    day= 1
    day2= 0


i = i+1
day= 185
day2= 0
temps = 1

for a in range (2002,2003):
    print a
    while day2 < 365:
        day2= day+7
        if day2 > 365:
            day2 = 365
        if a % 4 == 0 and day2 == 365:
            day2 = 366

        filen = data_in+'A'+str(a)+str(format(day,'03'))+str(a)+str(format(day2,'03'))+'.L3m_8D_CHL_chlor_a_4km_ZI'
        myfile = filen+str(i)+'_mean.npy'
        print myfile
        
        data = numpy.load(myfile)
        print data            
        plt.plot(temps, data, 'bs')
#        d[int(key)] = data
#        key = key +1
        temps = temps +1
        day= day+8
    if a == 2015 and day2 == 32:
        day2 = 365
    day= 1
    day2= 0

#plt.plot(temps, temps, '--bo')
plt.axis([1, temps, 0, 0.4])
plt.title('Valeurs moyennes de concentration en chlorophylle-a') 
plt.xlabel('Temps')
plt.ylabel('[chlor-a] en mg/m3')


plt.show()
print 'Fin'