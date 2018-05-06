import math
import sys

list = [] #definirla liste
list.append(1) #ajouter un element a une liste
print(list) #afficher la liste
print(list[0]) #afficher un element de la liste rq: commence par 0
list[0] = 2 #modifier une valeur avec son index
print(list[0])
del list[0] #supprime une valeur
print(len(list)) #compter le nb d'items
list.count(1) #compter le nb d'apparitions d'une valeur
list.append(1)
list.index(1) #permet de connaitre l'index d'une valeur
liste = [1, 2, 3, 4]
for chiffre in liste: #affichage boucle
	print(chiffre)
if 3 in liste: #savoir si un element est dans la liste
	print("vrai")


#http://apprendre-python.com/page-apprendre-listes-list-tableaux-tableaux-liste-array-python-cours-debutant
