#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Desc : Liste de noms
#
# Auteur : T.P.
# Date : 08/7/15

# ** Script en projet pour MODISA / SWF en 8 et 32 D (L3m) **
# ** Changer les variables par leur indice **

# ============= Imports =========================================================

import urllib

# ===============================================================================
# ============== Choisir des variables ==========================================

laps =[7,31][0]                         # 7 ou 31 jours de décalage (8D ou 32D)
day= 1                                  # Borne jour 1
day2= [8,32][0]                         # Borne jour 2 (pour 8D et 32D)
a2= int()                               # Borne Annee 2 ('a' est définie dans la boucle)
t1, t2 = [(1997, 2010),(2002,2015)][1]  # Pour boucle for (t1 et t2+1) pour SWF et MODISA
varnum= 0                               # 0,1,2,3 pour 8D ; 4,5,6,7 pour 32D || ordre : Chl,sst,poc,nsst

sat_path= ['swf','aqua'][1]                                                 # --> local directory
time_laps= ['8Day', 'Rolling_32_Day'][0]                                    # --> Web path
reso= ['4km', '9km', '4', '9'][1]                                           # --> Web & local path >> Verifier le nom des fichiers ('9' ou '9km') !
var_path= ['chl_8d','sst11mic_8d','poc_8d','nsst_8d',
      'chl_32d','sst11mic_32d','poc_32d','nsst_32d'][varnum]                # --> local directory                     
filler= ['8D_CHL_chlor_a_','8D_SST_sst_','8D_POC_poc_','8D_NSST_',
         'R32_CHL_chlor_a_','R32_SST_','R32_POC_poc_','R32_NSST_'][varnum]  # --> Web filename

print 'resolution -->', reso,'variable -->', var_path
path='/home/pressions/SATELITIME/data/FULL/'             # |
path = path+var_path+'/'+sat_path+'/'+reso+'/'           # --> save path (local)

# ===============================================================================
# =============== Boucle de téléchargement ======================================

for a in range (t1,t2+1):                   # Boucle de borne1 à borne2+1 (MODISA & SWF)
    print a
    a2 = a
    # --------------------------
    if a == 2002:              # Test MODISA
        day = 185
        day2 = day+laps
    else:
        day =1
        day2 =day+laps
    # ---------------------------
#    if a == 1997:               # Test SWF
#        day = 217
#        day2 = day+laps
#    else:
#        day =1
#        day2 = day+laps
    # ---------------------------
    while day <= 361:                       # 361 valable pour SWFS et MODISA (normalement).
        # ------------------- 
        if day2 > 365:                      # Test MODISA 8D
            day2 = 365
        if a % 4 == 0 and day == 365:
            day2 = 366
        # --------------------
#        if day == 337:                      # Test 32D (fichiers sur 2 années)
#            day2 = 3
#            a2=a+1
        # --------------------
#        if a % 4 == 0 and day == 337:       # Test 32D (pour années % par 4)
#            day2 = 2
#            a2=a+1
        url= 'http://oceandata.sci.gsfc.nasa.gov/cgi/getfile/'
        
        ##### Ici remplacer A par S ou inversement pour swFs et modisA #####
        #filen='A'+str(a)+str(format(day,'03'))+str(a)+str(format(day2,'03'))+'.L3m_8D_NSST_4.bz2'  #'.L3m_8D_SST_4.bz2' #'.L3m_8D_SST_4.bz2'
        filen='A'+str(a)+str(format(day,'03'))+str(a2)+str(format(day2,'03'))+'.L3m_'+filler+reso+'.bz2'  
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
        # ---------------------------------
        if a == 2015 and day2 > 176:        # --> MODISA 8 et 32 Stop
            day = 9999
        # ---------------------------------
#        if a == 2010 and day > 345:        # -- > SWF 8 et 32 Stop
#            day = 9999
        # ---------------------------------
    day= 1
    day2= day+laps
print 'Fin'

#Fin du script
