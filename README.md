# Projet_NSI

# Jeu du plus ou du moins

## Description

L'ordinateur choisis un nombre entre 1 et 100 et le joueur doit trouver le nombre choisis par l'ordinateur en utilisant le pincipe de la recherche dicotomique.
Si le nombre donné par le joueur est plus petit que le nombre choisis l'ordinateur renverra 'plus grand' inversement si le nombre choisis est trop grand l'ordinateur renverra 'plus petit'. Quand le joueur aura trouvé le nombre mysytère (-> nombre choisis par l'ordianteur), l'ordinateur renverra le nombre d'essais du joueur + son nom.

## Cahier journal

- Jour n°1 :

Début de la création d'un jeu utilisant la recherche dicotomique.
Language utilisé : python.

[plus_ou_moins.py](plus_ou_moins.py)


- Jour n°2:

Suite de la création du jeu. Ajout d'un nom pour le joueur, d'un mode de jeu avec des un nombre d'essais limité.


- Jour n°3:

Ajout d'un mode de jeu avec essais illimité, la partie s'arrete une fois que le joueur a trouver le nombre mystère, Choix de choisir entre les deux modes de jeux.
Tentative d'ajout d'un tableux de score en python.


- Jour n°4:

Création d'une base de donné en SQLITE pour les scores, Nom et le nombre mystère à trouver.

```sql
sqlite> CREATE TABLE IF NOT EXISTS score ("ID" INTEGER PRIMARY KEY, "Nom" TEXT, "Nbr_essais" INTEGER, "Nbr_mystère" TEXT);
```

Mise en place de l'ajout des joueurs en python.

- Jour n°5 (09/04/2021):

Création d'un compte github, édition du README.md

- Jour n°6 (13/04/2021):

Tentative d'utilisation de la fonction `ScoreSQL`.

- Jour n°7 (14/04/2021):

Ajout de la ligne `requete01 = "CREATE TABLE IF NOT EXISTS 'Score'('ID' INTEGER PRIMARY KEY, 'Nom' TEXT, 'Essais' INTEGER, 'Nbr mystère' INTEGER);"` dans la fonction `ScoreSQL`.

```sql
tgnsi_francois@lrg-ESPRIMO-P557:~/Bureau/projet$ sqlite3 score.db
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
sqlite> .headers ON
sqlite> .mode column
sqlite> .schema
CREATE TABLE score ("ID" INTEGER PRIMARY KEY, "Nom" TEXT, "Nbr_essais" INTEGER, "Nbr_mystère" TEXT);
sqlite> SELECT * FROM score;
ID                 Nom         Nbr_essais  Nbr_mystère
-----------------  ----------  ----------  -----------
17156204879061976  toto        5           16         
18342672012615565  ot          6           81         
32407199022071156  toto        5           16         
41126071367086791  toto        7           59         
62199492641392917  toto        7           86         
sqlite> SELECT * FROM score;
ID                Nom         Nbr_essais  Nbr_mystère
----------------  ----------  ----------  -----------
8789974074496604  jeff        8           83         
1715620487906197  toto        5           16         
1834267201261556  ot          6           81         
3240719902207115  toto        5           16         
4112607136708679  toto        7           59         
6219949264139291  toto        7           86         
```
réussite de la mise en place d'un tableau de score, mais nécessité d'ouvrir un terminal pour voir le tableau des scores

- Jour n°8 (16/04/2021):

rédaction du rapport de projet.
