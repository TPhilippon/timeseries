#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Desc : Liste de noms
#
# Auteur : T.P.
# Date : 15/2/15

#Premier script essai
#Tous les noms de fichier pour les années 2002 à 2015

# ============= Imports =========================================================

import urllib

# ===============================================================================
# ============== definition variables ===========================================

day= 1                          # Borne jour 1
day2= 32                        # Borne jour 2
a2= 8                           # Borne Annee 2 ('a' définie dans la boucle)
#varnum= 1                       # 0 -> 'chl_8d', 1 -> 'chl_32d'
#fillernum = 0                   # 0 ->chlor-a, 1->SST, 2->poc, 3->pic, 4->NSST

t1, t2 = 2002, 2015         # Pour boucle for (t1 et t2+1)

Reso= '4km'                                                            # Resolution : 9km, 4km
time_laps= ['8Day', 'Rolling_32_Day'][1]                               # Web path time laps
var_path= ['chl_8d','nsst_8d', 'poc_8d', 'sst11mic_8d', 'chl_32d'][4]  # path catalogue des données locales                     
sat_path= ['aqua', 'swf'][0]                                           # Satellite nom pour path local
filler= ['_CHL_chlor_a_', '_SST_sst_', '_POC_poc_', '_PIC_pic_', 'NSST_'][0]  # Pour filen(ame)

print 'resolution -->', Reso,'variable -->', var_path
path='/home/pressions/SATELITIME/data/FULL/'             # |
path = path+var_path+sat_path                            # --> save path (local)

# ===============================================================================
# =============== Boucle Download ===============================================

for a in range (t1,t2+1):                   # Boucle de borne1 à borne2+1 (AQUA MODIS)
#for a in range (1997,2011):                # Boucle de borne1 à borne2+1 (SEAWIFS)
    print a
    a2 = a
    if a == 2002:
        day = 161
        day2 = 192
    else:
        day =1
        day2 =32
    while day <= 361:                       # 361 valable pour seawifs et aqua modis (normalement).
        if a % 4 == 0 and day == 337:       # Pour 2004, 2008 et 2012.
            day2 = 2
            b=a+1
        if day == 337:                      # (Fichiers à cheval sur 2 années)
            day2 = 3
            b=a+1
       
        url= 'http://oceandata.sci.gsfc.nasa.gov/cgi/getfile/'

        #filen='A'+str(a)+str(format(day,'03'))+str(a)+str(format(day2,'03'))+'.L3m_8D_NSST_4.bz2'  #'.L3m_8D_SST_4.bz2' #'.L3m_8D_SST_4.bz2'
        filen='S'+str(a)+str(format(day,'03'))+str(a2)+str(format(day2,'03'))+'.L3m_'+filler+Reso+'.bz2'  
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
