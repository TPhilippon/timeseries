# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:33:04 2015

@author: upression1
"""
            #-------------------Scrip testeur



import matplotlib.pyplot as plt
import numpy as np
from numpy import *
import os
# -------------------------------------------------------------------------- 


#t1=np.linspace(0,5,10)
#t2=np.linspace(0,5,20)
#plt.plot(t1, t1, 'r--', t1, t1**2, 'bs', t2, t2**3, 'g^-')
#
#plt.show()

# ----------------------------------------------------------------
#x = arange(0.,10,0.1)
#a = cos(x)
#b = sin(x)
#c = exp(x/10)
#d = exp(-x/10)
#la = plt.plot(x,a,'b-',label='cosine')
#lb = plt.plot(x,b,'r--',label='sine')
#lc = plt.plot(x,c,'gx',label='exp(+x)')
#ld = plt.plot(x,d,'y-', linewidth = 5,label='exp(-x)')
#ll = plt.legend(loc='upper left')
#lx = plt.xlabel('xaxis')
#ly = plt.ylabel('yaxis')
#plt.show()
# ----------------------------------------------------------------
data_in ='/home/pressions/SATELITIME/data/chl_8d/hdf/'

files = os.listdir(data_in)
files.sort() 
print len(files) 


#day=[1,2,3,4,5,6]
#f=[3,6,8,9,10,12]
#labels = ['juin 2002', 'decembre 2002', 'juin 2003']
#a = plt.plot(day, f)
#plt.xticks(day, labels)


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



    # ---------------------------------------------------------------------------
#    if (myfile[5:8] == '185') or (myfile[5:8] == '360'):
#        date=date+[myfile[5:8]]
#        date = date + myfile[5:8]
    
    
        


#x = arange(0.,10.,0.1)
#y = sin(x)
#z = y+0.1
#zz = y-0.1
#ll = plt.plot(x,y)
#llz = plt.plot(x,z)
#llzz = plt.plot(x,zz)
#xl = plt.xlabel('horizontal axis')
#yl = plt.ylabel('vertical axis')
#ttl = plt.title('sine function')
#ax = plt.axis([-2, 12, -1.5, 1.5])
#grd = plt.grid(True)
#txt = plt.text(0,1.3,'here is some text')
#ann = plt.annotate('a point on curve',xy=(4.7,-1),xytext=(3,-1.3),arrowprops=dict(arrowstyle='->'))
#plt.show()

print 'fin'


