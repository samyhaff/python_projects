import numpy as np
import random
import math

board = np.zeros((20, 20))
affichage = np.empty((20, 20))

print(board[19, 19])

def Continue():
    reponse = input("Voulez vous continuez? ")
    if reponse == "oui":
        return True
    else:
        return False

#input
x = input("abssices:")
y = input("ordonnées: ")
while Continue() == True:
    x = input("abssices:")
    y = input("ordonnées: ")
    board[x, y] = 1

def affichge():
    for i in range(0, 20):
        for j in range(0, 20):
            if board[i, j] == 1:
                affichage[i, j] = "*"
            else:
                affichage[i, j] = "."

print(affichage)
                
    
