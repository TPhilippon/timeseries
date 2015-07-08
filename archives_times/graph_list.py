# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:33:04 2015

@author: upression1
"""



import matplotlib.pyplot as plt
import numpy as np




         #------------ Graphique

data_in ='/home/pressions/SATELITIME/sdatats/Graph_data/'


#files = os.listdir(data_in) #Liste les fichiers.
#files.sort() #Trie les fichiers.
#print len(files) #len = longueur de la liste de fichiers.


i = 1       #ZI concernée(s). Inclure nouvelle boucle pour plus de courbes sur 1 graphe.
key = 1    
day= 185
day2= 0
temps = 1  
l=[]
l2=[]

print "début boucle"

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
        
        data = np.load(myfile)
        print data            
        #plt.plot(temps, data, 'g^') # linestyle='--'
        
        l.insert(key,data)
        l2.insert(key,temps)
        
        key = key +1
        temps = temps +1
        day= day+8
    if a == 2015 and day2 == 32:
        day2 = 365
    day= 1
    day2= 0


print l2

plt.plot(l2, l, 'g^', linestyle='-')

i = i+1
day= 185
day2= 0
temps = 1
key = 1
l3=[]
l4=[]

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
        
        data = np.load(myfile)
        print data            

        l3.insert(key,data)
        l4.insert(key,temps)
        
        key = key +1
        temps = temps +1
        day= day+8
    if a == 2015 and day2 == 32:
        day2 = 365
    day= 1
    day2= 0

plt.plot(l4, l3, '--', linestyle='-')

plt.axis([1, temps, 0, 0.3])
plt.title('Valeurs moyennes de concentration en chlorophylle-a') 
plt.xlabel('Temps')
plt.ylabel('[chlor-a] : mg/m3')


plt.show()
print 'Fin'


