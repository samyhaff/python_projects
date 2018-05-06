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

Width = 500
Height = 500
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

n=0

for y in range(0,Hauteur-1):
    for x in range(0,Longueur):
        if Entrée[x]==0:
            Entrée[x]=n
            n+=random.randint(0,1)
    x=0
    while x<Longueur:
        n=x
        while Entrée[x]==Entrée[n] and n<Longueur-1:
            n+=1
        Sortie[random.randint(x,n)]=Entrée[x]
        x=n
    for x in range(0,Longueur):
        X=x*Taille
        Y=y*Taille
        pygame.draw.rect(screen, (v%256,0,0), (X-l,Y-l,Taille,Taille), 0)
        pygame.display.flip()
    Entrée=Sortie[:]


    
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


pygame.quit() 
