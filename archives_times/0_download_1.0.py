#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Desc : Liste de noms
#
# Auteur : T.P.
# Date : 15/2/15

#Premier script essai
#Tous les noms de fichier pour les années 2002 à 2015

# ============= Imports ====================

import urllib

# =========================================
# ============== def variables ============

Reso= '4km'                     # 9km ## 4km
Var= 'chl_8d'                   # chlor ## SST ## NSST ## SST4...
filler= 'R32_CHL_chlor_a_'      # SST4_4 ## CHL_chlor_a_ ## NSST_sst_ ## SST_4 ## ...

day= 1
day2= 32
b= 8
counter=1

print 'resolution -->', Reso,'variable -->', Var
path= '/home/pressions/SATELITIME/data/FULL/'
path = path+Var+'/R32/'

# =========================================
# =============== Boucle DL ===============
for a in range (2002,2016):                 # La valeur 'a' s'arrêtera à 2015
#for a in range (1997,2011):
    print a
    b = a
    if a == 2002:
        day = 161
        day2 = 192
    else:
        day =1
        day2 =32
    while day <= 361:
        if day2 > 360:                      # Fichiers à cheval sur 2 années.
            day2 = 3
            b=a+1
        if a % 4 == 0 and day2 > 360:       # Pour 2004, 2008 et 2012.
            day2 = 2
            b=a+1
       
        url= 'http://oceandata.sci.gsfc.nasa.gov/cgi/getfile/'

        #filen='A'+str(a)+str(format(day,'03'))+str(a)+str(format(day2,'03'))+'.L3m_8D_NSST_4.bz2'  #'.L3m_8D_SST_4.bz2' #'.L3m_8D_SST_4.bz2'
        filen='A'+str(a)+str(format(day,'03'))+str(b)+str(format(day2,'03'))+'.L3m_'+filler+Reso+'.bz2'  
        #'.L3m_8D_POC_poc_4km.bz2'
        #'.L3m_8D_NSST_4.bz2'
        #'.L3m_8D_CHL_chlor_a_4km.bz2'
        #L3m_8D_CHL_chlor_a_9km.bz2
        print 'Getting', url+filen, '.........', path+filen
# ========================== Télégarchement ===============================
        urllib.urlretrieve(url+filen,path+filen)           # -----> Téléchargement
# =========================================================================
        day= day+8
        day2= day2+8
        if a == 2015 and day2 == 168:
            day = 9999
    day= 1
    day2= 32
print 'Fin'

#Fin du script
