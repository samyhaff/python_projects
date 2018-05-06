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
Taille = 2

Longueur=Width//Taille
Hauteur=Height//Taille
l = Taille//2

Grille = np.zeros([Hauteur, Longueur])

screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Maze Serpent")
done = False
clock = pygame.time.Clock()
screen.fill(FOND)

Init=True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if Init:
        for y in range(0,Hauteur,2):
            for x in range(0,Longueur,2):
                Grille[y,x]=1
                pygame.draw.rect(screen, COULEUR, (x*Taille-l,y*Taille-l,Taille,Taille), 0)
                if random.randint(0,3)==0:
                    Grille[y-1,x]=1
                    Grille[y+1,x]=1
                    pygame.draw.rect(screen, COULEUR, (x*Taille-l,(y-1)*Taille-l,Taille,Taille), 0)
                    pygame.draw.rect(screen, COULEUR, (x*Taille-l,(y+1)*Taille-l,Taille,Taille), 0)
                if random.randint(0,3)==0:
                    Grille[y,x-1]=1
                    Grille[y,x+1]=1
                    pygame.draw.rect(screen, COULEUR, ((x-1)*Taille-l,y*Taille-l,Taille,Taille), 0)
                    pygame.draw.rect(screen, COULEUR, ((x+1)*Taille-l,y*Taille-l,Taille,Taille), 0)
        x=Longueur//2
        y=Hauteur//2
        r=0
        Init=False
        
    if Init==False:
        
            
        pygame.draw.rect(screen, RED, (x*Taille-l,y*Taille-l,Taille,Taille), 0) 
    pygame.display.flip()
pygame.quit()
