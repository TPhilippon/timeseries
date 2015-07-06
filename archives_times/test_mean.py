# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 12:01:56 2015

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




         #------------ Traitement mathématique (moyenne) et sauvegarde en .npy

data_in ='/home/pressions/SATELITIME/sdatats/Graph_data/'


#files = os.listdir(data_in) #Liste les fichiers.
#files.sort() #Trie les fichiers.
#print len(files) #len = longueur de la liste de fichiers.

#d = {}
#i = 1     #ZI concernée(s). Inclure nouvelle boucle pour x courbe sur 1 graphe.
#key = 1     #Compteur pour le dictionnaire.

print "début boucle"

day= 185
day2= 0

for a in range (2002,2003):
    print a
    while day2 < 220:
        day2= day+7
        if day2 > 365:
            day2 = 365
        if a % 4 == 0 and day2 == 365:
            day2 = 366

        filen = data_in+'A'+str(a)+str(format(day,'03'))+str(a)+str(format(day2,'03'))+'.L3m_8D_CHL_chlor_a_4km_ZR'   #
        myfile = filen+'.npy'
        
        print myfile            
        data = numpy.load(myfile)
        data_mean = numpy.mean(data)
        print data_mean        
        numpy.save(filen+'_mean', data_mean)
        #d[str(key)+'ZI'+str(i)] = data_mean
        #print d[str(key)+'ZI'+str(i)]
        #key = key +1
        

        day= day+8
    if a == 2015 and day2 == 32:
        day2 = 365
    day= 1
    day2= 0


print 'fin'
#print d
#
#temps = 1
#
#plt.axis([1, 4, 0.01, 10])
#plt.title('Test')
#for f in d:
#        
#    plt.plot(temps, f, 'bs')
#    temps = temps +1
#
#
#plt.show()