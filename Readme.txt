* Voir le script 1_download (dossier video) pour le t�l�chargement.

* 






Algorithme de programmation

# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:40:24 2015

@author: upression1
"""
## _ _ _ _ _ _
##(- Tester un script de multithreading sur spyder. -)
##Programme I.
##_ _ _ _ _ _ Boucle 1
##1 Zone Cara�be : Reprendre le d�coupage de la M�dit et remplacer les 
#coordonn�es rentr�es par un � print � qui permet de choisir les 4 valeurs 
#de coordonn�es  Pour la saisie manuelle des coordonn�es de chaque zone 
#(applicable � d�autres).
##	Indiquer chemin des fichiers.
##	Adapter le script de d�coupage.
##	Saisie manuelle des 4 coordonn�es.
##	D�couper et cr�er nouveau fichier.
##_ _ _ _ _ _ Fin Boucle 1 -> Boucle 2
##2 Cadre rouge pixels � analyser : s�lectionner un cadre de pixels � analyser 
#+ cadre rouge � tracer sur les m�mes coordonn�es. Choix manuel des 4 valeurs. 
#+ V�rification avec affichage 1 fichier.
##	Chemin nouveaux fichiers d�coup�s.
##	Choix coordonn�es.
##	S�lection pixels dans le cadre. 
##	Trac� cadre rouge.
##	M�moriser les pixels � traiter.
##_ _ _ _ _ _ 
##3 Cadre jaune pixels exclus : Idem que 2) avec pixels � exclure OU 
#d�calage du cadre rouge pour �viter les zones � exclure pr�s des c�tes.
##	Idem que 2) mais pixels exclus et cadre jaune.
##
##_ _ _ _ _ _ Fin boucle 2
##4 Afficher r�sultat : image avec les 2 cadres rouge et jaune. 
##_ _ _ _ _ _ Boucle 3
##5 Traitement des donn�es contenues dans les pixels : Moyennes sous forme
# de graphique, etc.
##	Calcul des moyennes.
##	Affichage sous forme de graphique.
##_ _ _ _ _ _ 
##
## 
##Programme II.
##_ _ _ _ _ _ 
##Hors programmation : d�finir des seuils pour le panache de [Chlorophylle-a].
##_ _ _ _ _ _ Boucle 1
##1 Utiliser les fichiers Cara�be du I.1.
##	Rentrer la valeur seuil pour le panache.
##	Cr�er isoligne pour d�limiter le panache. 
##	L�gende et �chelle � ins�rer.
##	Interpolation pour lisser l�affichage.
##_ _ _ _ _ _Fin boucle 1
##2 Animation.
##_ _ _ _ _ _ 
#

