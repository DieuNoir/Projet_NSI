# Projet_NSI

# Jeu du plus ou du moins

## Description

L'ordinateur choisis un nombre entre 1 et 100 et le joueur doit trouver le nombre choisis par l'ordianteur en utilisant le pincipe de la recherche dicotomique

## Cahier journal

- Jour n°1 :

Début de la création d'un jeu utilisant la recherche dicotomique.
Language utiliser : python.

[plus_ou_moins.py](plus_ou_moins.py)


- Jour n°2:

Suite de la création du jeu. Ajout d'un nom pour le joueur, d'un mode de jeu avec des un nombre d'essais limité.


- Jour n°3:

Ajout d'un mode de jeu avec essais illimité, la partie s'arrete une fois que le joueur a trouver le nombre mystère, Choix de choisir entre les deux modes de jeux.
Tentative d'ajout d'un tableux de score en python.


- Jour n°4:

Création d'une base de donné en SQLITE pour les scores, Nom et le nombre mystère à trouver.

sqlite> CREATE TABLE IF NOT EXISTS score ("ID" INTEGER PRIMARY KEY, "Nom" TEXT, "Nbr_essais" INTEGER, "Nbr_mystère" TEXT);

Mise en place de l'ajout des joueurs en python.

- Jour n°5:

