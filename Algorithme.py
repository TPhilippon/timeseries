# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:40:24 2015

@author: upression1
"""
## _ _ _ _ _ _
##(- Tester un script de multithreading sur spyder. -)
##Programme I.
##_ _ _ _ _ _ Boucle 1
##1 Zone Caraïbe : Reprendre le découpage de la Médit et remplacer les 
#coordonnées rentrées par un « print » qui permet de choisir les 4 valeurs 
#de coordonnées  Pour la saisie manuelle des coordonnées de chaque zone 
#(applicable à d’autres).
##	Indiquer chemin des fichiers.
##	Adapter le script de découpage.
##	Saisie manuelle des 4 coordonnées.
##	Découper et créer nouveau fichier.
##_ _ _ _ _ _ Fin Boucle 1 -> Boucle 2
##2 Cadre rouge pixels à analyser : sélectionner un cadre de pixels à analyser 
#+ cadre rouge à tracer sur les mêmes coordonnées. Choix manuel des 4 valeurs. 
#+ Vérification avec affichage 1 fichier.
##	Chemin nouveaux fichiers découpés.
##	Choix coordonnées.
##	Sélection pixels dans le cadre. 
##	Tracé cadre rouge.
##	Mémoriser les pixels à traiter.
##_ _ _ _ _ _ 
##3 Cadre jaune pixels exclus : Idem que 2) avec pixels à exclure OU 
#décalage du cadre rouge pour éviter les zones à exclure près des côtes.
##	Idem que 2) mais pixels exclus et cadre jaune.
##
##_ _ _ _ _ _ Fin boucle 2
##4 Afficher résultat : image avec les 2 cadres rouge et jaune. 
##_ _ _ _ _ _ Boucle 3
##5 Traitement des données contenues dans les pixels : Moyennes sous forme
# de graphique, etc.
##	Calcul des moyennes.
##	Affichage sous forme de graphique.
##_ _ _ _ _ _ 
##
## 
##Programme II.
##_ _ _ _ _ _ 
##Hors programmation : définir des seuils pour le panache de [Chlorophylle-a].
##_ _ _ _ _ _ Boucle 1
##1 Utiliser les fichiers Caraïbe du I.1.
##	Rentrer la valeur seuil pour le panache.
##	Créer isoligne pour délimiter le panache. 
##	Légende et échelle à insérer.
##	Interpolation pour lisser l’affichage.
##_ _ _ _ _ _Fin boucle 1
##2 Animation.
##_ _ _ _ _ _ 
#
