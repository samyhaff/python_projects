import pygame
import numpy as np
import math
import random
from pygame.locals import *
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

COULEUR=GREEN
FOND=BLACK

Width = 800
Height = 800
Taille = 100

Longueur=Width//Taille
Hauteur=Height//Taille
l = Taille//2

Entrée=[0]*Longueur
Sortie=[0]*Longueur

screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Eller's Maze")
done = False
clock = pygame.time.Clock()
screen.fill(FOND)

Grille=[]
Entrée=[0]*Longueur
for x in range(0,Longueur):
    if Entrée[x]==0:
        Entrée[x]=x+1

m=0
for y in range(0,Hauteur-1):
    m=(y+1)*Longueur+m
    for x in range(0,Longueur-1):
        if random.randint(0,10)!=0:
            Entrée[x]=Entrée[x+1]
    x=0
    while x<Longueur-1:
        n=x
        while n<Longueur:
            if Entrée[x]==Entrée[n]:
                n+=1
            else:
                Sortie[random.randint(x,n-1)]=Entrée[x]
                x=n
        x=x+1
        Sortie[Longueur-1]=Entrée[Longueur-1]
    for x in range(0,Longueur):
        if Sortie[x]==0:
            Sortie[x]=m
            m=m+1
    for x in range(0,Longueur):
        X=x*Taille
        Y=y*Taille
        v=Entrée[x]
        pygame.draw.rect(screen, (100*v%256,50*v%256,25*v%256), (X-l,Y-l,Taille,Taille), 0)
        pygame.display.flip()
    Entrée=Sortie[:]
    Grille.append(Entrée)

    
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


pygame.quit() 

