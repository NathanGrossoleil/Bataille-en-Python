#Jeu de la bataille
#Samuel Ribes--Chauvet, Nathan Grossoleil

import random
import time

#Paquet de 52 cartes
cartes52 = [
    (2, '2 de pique'), (2, '2 de trèfle'), (2, '2 de carreau'), (2, '2 de coeur'),
    (3, '3 de pique'), (3, '3 de trèfle'), (3, '3 de carreau'), (3, '3 de coeur'),
    (4, '4 de pique'), (4, '4 de trèfle'), (4, '4 de carreau'), (4, '4 de coeur'),
    (5, '5 de pique'), (5, '5 de trèfle'), (5, '5 de carreau'), (5, '5 de coeur'),
    (6, '6 de pique'), (6, '6 de trèfle'), (6, '6 de carreau'), (6, '6 de coeur'),
    (7, '7 de pique'), (7, '7 de trèfle'), (7, '7 de carreau'), (7, '7 de coeur'), 
    (8, '8 de pique'), (8, '8 de trèfle'), (8, '8 de carreau'), (8, '8 de coeur'), 
    (9, '9 de pique'), (9, '9 de trèfle'), (9, '9 de carreau'), (9, '9 de coeur'),
    (10, '10 de pique'), (10, '10 de trèfle'), (10, '10 de carreau'), (10, '10 de coeur'),
    (11, 'valet de pique'), (11, 'valet de trèfle'), (11, 'valet de carreau'), (11, 'valet de coeur'),
    (12, 'dame de pique'), (12, 'dame de trèfle'), (12, 'dame de carreau'), (12, 'dame de coeur'),
    (13, 'roi de pique'), (13, 'roi de trèfle'), (13, 'roi de carreau'), (13, 'roi de coeur'),
    (14, 'as de pique'), (14, 'as de trèfle'), (14, 'as de carreau'), (14, 'as de coeur')]

#Paquet de 32 cartes
cartes32 = [
    (7, '7 de pique'), (7, '7 de trèfle'), (7, '7 de carreau'), (7, '7 de coeur'), 
    (8, '8 de pique'), (8, '8 de trèfle'), (8, '8 de carreau'), (8, '8 de coeur'), 
    (9, '9 de pique'), (9, '9 de trèfle'), (9, '9 de carreau'), (9, '9 de coeur'),
    (10, '10 de pique'), (10, '10 de trèfle'), (10, '10 de carreau'), (10, '10 de coeur'),
    (11, 'valet de pique'), (11, 'valet de trèfle'), (11, 'valet de carreau'), (11, 'valet de coeur'),
    (12, 'dame de pique'), (12, 'dame de trèfle'), (12, 'dame de carreau'), (12, 'dame de coeur'),
    (13, 'roi de pique'), (13, 'roi de trèfle'), (13, 'roi de carreau'), (13, 'roi de coeur'),
    (14, 'as de pique'), (14, 'as de trèfle'), (14, 'as de carreau'), (14, 'as de coeur')]

class File:
    def __init__(self):
        '''
        Crée une file vide
        '''
        self.contenu = []

    def est_vide(self):
        '''
        Renvoie un booléen indiquant si la file est vide
        '''
        return self.contenu == []

    def enfiler(self, elt):
        '''
        Ajoute l'élément elt à la fin de la file
        '''
        self.contenu = [elt] + self.contenu

    def defiler(self):
        '''
        Retire et retourne l'élément a la fin de la file
        '''
        if self.est_vide():
            raise IndexError('On ne peut pas défiler une file vide')
        return self.contenu.pop()

    def sommet(self):
        '''
        Renvoie l'élément du sommet de la file, sans l'enlever
        '''
        if self.est_vide():
            raise IndexError("une file vide n'a pas de sommet")
        return self.contenu[0]

    def __str__(self):
        return str(self.contenu)

def jeu():
    '''
    Fonction jeu qui cree le jeu de la bataille a partir d'un paquet de 52 ou  32 cartes
    '''
    print('                           JEU DE LA BATAILLE')
    print()
    rep_cartes = int(input('Avec combien de cartes voulez-vous jouer ? 52 ou 32 ?'))  #question pour savoir avec un jeu de combien de carte il veule jouer
    while rep_cartes != 52 and rep_cartes != 32:
        rep_cartes = int(input('Avec combien de cartes voulez-vous jouer ? 52 ou 32 ?'))
    
    if rep_cartes == 52:
        cartes = cartes52
    elif rep_cartes == 32:
        cartes = cartes32

    rep_vitesse = str(input('Voulez-vous que les cartes défilent rapidement ?'))  #question pour savoir si il veule jouer rapidement ou pas
    while rep_vitesse != 'oui' and rep_vitesse != 'non': 
        rep_vitesse = str(input('Voulez-vous que les cartes défilent rapidement ?'))
        
    paquet1 = File()  #creation du paquet du premier joueur
    paquet2 = File()  #creation du paquet du deuxième joueur

    bataille1 = File()  #contient ce que le premier joueur découvre devant lui
    bataille2 = File()  #contient ce que le deuxième joueur découvre devant lui

    random.shuffle(cartes) #melange des cartes
    for i in range(len(cartes)//2):
        paquet1.enfiler(cartes[i]) #distribution des cartes dans le paquet 1
    for i in range(len(cartes)//2):
        paquet2.enfiler(cartes[(-i)-1]) #distribution des cartes dans le paquet 2
        
    print()
    while not paquet1.est_vide() and not paquet2.est_vide():
        if rep_vitesse == 'non':
            time.sleep(.2)
        bataille1.enfiler(paquet1.defiler()) #decouvre la premiere carte du paquet1 dans ce paquet
        bataille2.enfiler(paquet2.defiler()) #decouvre la premiere carte du paquet2 dans ce paquet


        print('Carte joueur 1 : ', bataille1.sommet()[1]) #défausse cartes
        print('Carte joueur 2 : ', bataille2.sommet()[1])

        print('Taille paquet joueur 1 : ', len(paquet1.contenu)) #taille paquets
        print('Taille paquet joueur 2 : ', len(paquet2.contenu))


        
        
        if bataille1.sommet()[0] == bataille2.sommet()[0]: #cas de bataille si les cartes sont pareil
            print('---------------------------------> BATAILLE')
            
            if paquet1.est_vide() or paquet2.est_vide(): #le programme s'arrete si le paquet 1 ou le paquet 2 esr vide
                break
            #on tire les cartes qui seront cachées
            bataille1.enfiler(paquet1.defiler())
            bataille2.enfiler(paquet2.defiler())
            print('---------------------- carte caché joueur 1: ', bataille1.sommet()[1])
            print('---------------------- carte caché joueur 2: ', bataille2.sommet()[1])
         

        elif bataille1.sommet()[0] > bataille2.sommet()[0]: #lorsque la carte du joueur 1 est supérieure a celle du joueur 2
            print('Joueur 1 remporte la manche')
            while not bataille1.est_vide():
                paquet1.enfiler(bataille1.defiler()) #le joueur 1 recupere les deux cartes 
                paquet1.enfiler(bataille2.defiler()) #et les enfile a la fin de son paquet
                print()

        elif bataille1.sommet()[0] < bataille2.sommet()[0]: #lorsque la carte du joueur 2 est supérieure a celle du joueur 1
            print('Joueur 2 remporte la manche')
            while not bataille1.est_vide():
                paquet2.enfiler(bataille1.defiler()) #le joueur 2 recupere les deux cartes 
                paquet2.enfiler(bataille2.defiler()) #et les enfile a la fin de son paquet
                print()
    print()
    if paquet1.est_vide():
        print('                    VICTOIRE DU JOUEUR 2') #renvoie le vainqueur en fonction du
    if paquet2.est_vide():                                #paquet qui est vide
        print('                    VICTOIRE DU JOUEUR 1')     
       
jeu() #initialise le jeu


    



