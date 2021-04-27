# Rapport de projet



## I \ Introduction

L'ordinateur choisis un nombre entre 1 et 100 et le joueur doit trouver le nombre choisis par l'ordinateur en utilisant le pincipe de la recherche dicotomique. 

J'ai choisi ce projet car  lorsque j'était en cours de math, nous en avons un petit peu parlé et j'ai trouver cela intéressant et j'ai donc voulu le mettre en pratique avec python ou en C++.

## II \ Cahier des charges

Mon programme doit lorsque le joueur aura trouvé le nombre mysytère (-> nombre choisis par  l'ordianteur), l'ordinateur renverra le nombre d'essais du joueur + son  nom (pour le jeu n°1) et renverra un message félicitant le joueur avec son nom pour avoir trouver le nombre mystère en un nombre limité (pour le jeux n°2).

Les solutions techniques choisies sont comme language de programmation le python, avec l'utilisation des modules `random` et `sqlite3` et l'utilisation du logiciel ***Thonny***.

## III \ recherche documentaire

Les éléments dont j'ai eu besoin pour la réalisation du projet sont **mon cours de maths**, 

## IV \ Réalisation

J'ai tout d'abord fait des recherches sur la recherche dicotomique via mon cours de maths, 

L'ordinateur choisis un nombre entre 1 et 100 et le joueur doit trouver le nombre choisis par l'ordinateur, si le nombre est plus grand que le nombre mystère alors le programme renverra que son nombre est trop grand, à l'inverse si le nombre est plus petit que le nombre mystère alors le programme renverra que son nombre est trop petit. 

## V \ Fonctionnement

Le programme complet fonctionne toujours, cepandant il peut y avoir des problèmes avec le jeu n°2 qui ne prend plus en compte le nombre d'essais limité et la fonction `ScoreSQL()`, où il est nécessaire d'ouvrir un terminal et lancer  `sqlite3 score.db` puis utiliser la requête `SELECT * FROM score` pour pouvoir avoir accès au tableau de score.

## VI \ Amélioration

Ce qui peut être améliorer est : 

- de faire en sorte de pouvoir consulter le tableau de score lorsque l'on en a envie,

- d'améliorer le code du programme mettre dans des fonctions le jeu n°1 et n°2,
- faire une interface graphique,
- de faire en sorte que l'encadrement change avec le nombre choisi par le joueur.



## Conclusion

J'ai bien apprécier l'idée de faire un projet (qui de base est simple) mais de devoir rajouter un tableau de score m'a bien prit la tête. Ce travail m'apporté qu'il faut voir les choses en grand, de ne pas réduire les possiblité.



## Annexe

``````python
from random import *
from sqlite3 import *	# Importation des modules random et sqlite3


nom = input("Comment t'appelle-tu ? ")	 # On demande le pseudo du joueur
jeu = input("Il y a deux mode de jeux tape 1 pour le premier et 2 pour le deuxième : ")	# On demande le choix du jeux 


mystery_number = randint(1, 100)	# L'ordinateur choisi un nombre compris sur l'intervalle [1, 100]

def ScoreSQL():
    global nom, essais, mystery_number
    bdd = connect("score.db")
    curseur = bdd.cursor()  # on crée un curseur
    
    requete01 = "CREATE TABLE IF NOT EXISTS 'Score'('ID' INTEGER PRIMARY KEY, 'Nom' TEXT, 'Essais' INTEGER, 'Nbr mystère' INTEGER);"
    
    requete = "INSERT INTO Score VALUES("
    requete += str(randint(1, 2**56)) + " , "
    requete += "'" + nom + "' , "
    requete += str(essais) +" , "
    requete += str(mystery_number)
    requete += ");"
    
    curseur.execute(requete01)
    curseur.execute(requete)
    print(curseur.fetchall())   # récupération de l'ensemble des résultats en une seule liste
    
    bdd.commit()
    curseur.close()
    bdd.close()

if jeu == "1":
    
    print("Ton objectif est de trouver le nombre choisis par l'ordianteur avec le moins d'essais possible.")
    print("Bonne Chance !\n")	# Le programme lance le jeu n°1
    
    b = int(input("Choisi un nombre compris entre 1 et 100 : "))
    essais = 0
    
    while b != mystery_number:
        
        if b > mystery_number:
            print("plus petit\n")
            b = int(input("Choisi un nombre compris entre 1 et 100 : "))
            essais += 1

        if b < mystery_number:
            print("plus grand\n")
            b = int(input("Choisie un nombre compris entre 1 et 100 : "))
            essais += 1

        if b == mystery_number:
            print( nom ,"a réussi en ", essais, "essais")	# renvois le nom + les essais du joueur
            ScoreSQL()
            break

if jeu == "2":
    
    print("Ton objectif est de trouver le nombre choisis par l'ordianteur en 5 essais.")
    print("Bonne Chance !\n")	# Le programme lance le jeu n°2
    
    b = int(input("Choisi un nombre compris entre 1 et 100 : "))
    max_try = 4		# on défini un nombre d'essais limité

    while b != mystery_number:
    
        if b > mystery_number:
            max_try -= 1 	# On décremente le compteur max_try de 1
            print("plus petit\n")
            b = int(input("Choisi un nombre compris entre 1 et 100 : "))
            

        if b < mystery_number:
            max_try -= 1 	# On décremente le compteur max_try de 1
            print("plus grand\n")
            b = int(input("Choisie un nombre compris entre 1 et 100 : "))
            

        if b == mystery_number:
            #ScoreSQL()
            print( nom ,"a réussi. FÉLICITATION !!!!") 	# On félicite le joueur
            break
    
        if max_try == 0:
            print("RECOMMENCE !!!")
            break

#def score():           # tentative d'une fonction score en python !
#    NL = []
#    SL = []
#    if jeu == "1" or jeu == "2":
#        NL.append(nom)
#        SL.append(essais)
#    for i in [x for x in NL if x in SL]:
#        print(i)
``````
