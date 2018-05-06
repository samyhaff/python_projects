import math
import random
import pygame
import numpy as np
from pygame.locals import *
pygame.init()

Width=700
Height=700
Taille=10

l=Taille//5

Longueur=Width//Taille
Hauteur=Height//Taille

Liste1 = np.zeros([Hauteur, Longueur])
Liste2 = np.zeros([Hauteur, Longueur])

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

COULEUR=GREEN
FOND=BLACK

size=(Width,Height)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("The Game of Life")
 
done = False
Etape=0

clock = pygame.time.Clock()
screen.fill(FOND)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                Etape=(Etape+1)%2
            if event.key == K_ESCAPE:
                Liste1 = np.zeros([Hauteur, Longueur])
                Liste2 = np.zeros([Hauteur, Longueur])
                screen.fill(FOND)
                Etape=0               
        if Etape==0:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x = event.pos[0]//Taille
                y = event.pos[1]//Taille
                X=x*Taille
                Y=y*Taille
                Liste1[y,x]=(Liste1[y,x]+1)%2
                if Liste1[y,x]==0:
                    pygame.draw.rect(screen, FOND, (X-l,Y-l,Taille,Taille), 0)
                else:
                    pygame.draw.rect(screen, COULEUR, (X-l,Y-l,Taille,Taille), 0)
    if Etape==1:
        Liste2=np.copy(Liste1)
        for y in range(1,Hauteur-1):
            for x in range(1,Longueur-1):
                Voisine=0
                for j in range(-1,2):
                    for i in range(-1,2):
                        if Liste1[y+j,x+i]==1:
                            if i!=0 or j!=0:
                                Voisine=Voisine+1
                if Voisine<2 or Voisine>3:
                    Liste2[y,x] = 0
                if Voisine==3:
                    Liste2[y,x] = 1
                X=x*Taille
                Y=y*Taille
                if Liste2[y,x]==0:
                    pygame.draw.rect(screen, FOND, (X-l,Y-l,Taille,Taille), 0)
                else:
                    pygame.draw.rect(screen, COULEUR, (X-l,Y-l,Taille,Taille), 0)
        Liste1=np.copy(Liste2)
    pygame.display.flip()
    clock.tick(1000000)
pygame.quit()
