# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 14:05:46 2015

@author: upression1
"""

import numpy as np
import matplotlib
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

         #------------ Import / lecture npy data
         
data_in ='/home/pressions/SATELITIME/sdatats/Graph_data/'
#files = os.lisdir(data_in)
#files.sort()

i = 1       


day= 185
day2= 0
temps = 1

for a in range (2002,2003):
    print a
    while day2 < 248:
        day2= day+7
        if day2 > 365:
            day2 = 365
        if a % 4 == 0 and day2 == 365:
            day2 = 366
         
        filen = data_in+'A'+str(a)+str(format(day,'03'))+str(a)+str(format(day2,'03'))+'.L3m_8D_CHL_chlor_a_4km_'
        myfile = filen+'ZR.npy'
        print myfile
        
        data =np.load(myfile)
        data2=np.array(data)
         
         #------------ Isoligne
         
        iso = data2[ data2 > 1]
        matplotlib.rcParams['xtick.direction']='out'
        matplotlib.rcParams['ytick.direction']='out'
        
        delta = 0.025
        x = np.arange(0.1, 2.0, delta)
        y = np.arange(0.1, 2.0, delta)
        
        X, Y = np.meshgrid(x,y)
        Z =mlab.bivariate_normal(X, Y, data2)
        
         
         #------------ Affichage
         
        plt.figure()
        CS = plt.contour (X, Y, Z)
        plt.clabel(CS, inline=1, fontsize=10)
        plt.title('test')
        
        plt.show()
         
         