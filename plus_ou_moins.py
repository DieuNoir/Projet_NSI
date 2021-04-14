from random import *
from sqlite3 import *


nom = input("Comment t'appelle-tu ? ")
jeu = input("Il y a deux mode de jeux tape 1 pour le premier et 2 pour le deuxième : ")


mystery_number = randint(1, 100)

def ScoreSQL():
    global nom, essais, mystery_number
    bdd = connect("score.db")
    curseur = bdd.cursor()
    
    requete01 = "CREATE TABLE IF NOT EXISTS 'Score'('ID' INTEGER PRIMARY KEY, 'Nom' TEXT, 'Essais' INTEGER, 'Nbr mystère' INTEGER);"
    
    requete = "INSERT INTO Score VALUES("
    requete += str(randint(1, 2**56)) + " , "
    requete += "'" + nom + "' , "
    requete += str(essais) +" , "
    requete += str(mystery_number)
    requete += ");"
    
    curseur.execute(requete01)
    curseur.execute(requete)
    print(curseur.fetchall())
    
    bdd.commit()
    curseur.close()
    bdd.close()

if jeu == "1":
    
    print("Ton objectif est de trouver le nombre choisis par l'ordianteur avec le moins d'essais possible.")
    print("Bonne Chance !\n")
    
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
            print( nom ,"a réussi en ", essais, "essais")
            ScoreSQL()
            break

if jeu == "2":
    
    print("Ton objectif est de trouver le nombre choisis par l'ordianteur en 5 essais.")
    print("Bonne Chance !\n")
    
    b = int(input("Choisi un nombre compris entre 1 et 100 : "))
    max_try = 4

    while b != mystery_number:
    
        if b > mystery_number:
            max_try -= 1
            print("plus petit\n")
            b = int(input("Choisi un nombre compris entre 1 et 100 : "))
            

        if b < mystery_number:
            max_try -= 1
            print("plus grand\n")
            b = int(input("Choisie un nombre compris entre 1 et 100 : "))
            

        if b == mystery_number:
            #ScoreSQL()
            print( nom ,"a réussi. FÉLICITATION !!!!")
            break
    
        if max_try == 0:
            print("RECOMMENCE !!!")
            break

#def score():
#    NL = []
#    SL = []
#    if jeu == "1" or jeu == "2":
#        NL.append(nom)
#        SL.append(essais)
#    for i in [x for x in NL if x in SL]:
#        print(i)

