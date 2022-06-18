# Knapsack-Problem

***Livrable du Projet 7 du parcours D-A Python d'OpenClassrooms : 
calcul de la meilleure combinaison d'actions en fonction de leurs bénéfices***

- ***Bruteforce***

- ***Programmation dynamique (algorithme du sac à dos)***

_Testé sous Windows 10 - Python version 3.9.5_

## Initialisation du projet (Installation du projet et de ses dépendences.

    git clone https://github.com/Ryotari/Knapsack-Problem.git

    cd Knapsack-Problem
    python -m venv env 
    env\scripts\activate

    pip install -r requirements.txt

### Bruteforce

    python bruteforce.py

L'algorithme bruteforce ne traîte que les données du fichier "bruteforce_test.csv", contenant 20 actions. Les datasets 1 et 2 résulteraient à un temps d'exécution extrêmement long.

### Programmation dynamique (Problème du Sac à Dos)

    python optimized.py 

Il s'agit ici d'un algorithme glouton, qui vise à trier les actions par bénéfices (dans l'ordre décroissant), puis parcourir la liste pour ajouter les actions une à une à notre meilleure combinaison, si notre argent restant nous le permet. 