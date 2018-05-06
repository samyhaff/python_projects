import math
import random
import pygame
import numpy as np
from pygame.locals import *
pygame.init()

Width=700
Height=700
Taille=10

l=Taille//2

Longueur=Width//Taille
Hauteur=Height//Taille

Liste = np.zeros([Hauteur, Longueur])

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

clock = pygame.time.Clock()
screen.fill(FOND)

x=Longueur//2
y=Hauteur//2
r=0

def Tourner(Rotation):
    Rotation=(Rotation+1)%4

def Avancer(x,y,Rotation):
    if Rotation==0:
        x=x-1
    if Rotation==1:
        y=y+1
    if Rotation==2:
        x=x+1
    if Rotation==3:
        y=y+1

def Téléporter(x,y):
    if x>Longueur:
        x=0
    if y>Hauteur:
        y=0
    if x<0:
        x=Longueur
    if y<0:
        y=Hauteur
    
def Mur(x,y):
    if x>Longueur:
        x=Longueur
    if y>Hauteur:
        y=Hauteur
    if x<0:
        x=0
    if y<0:
        y=0

def Détecter(x,y):
    if Liste[y,x]==0:
        return False
    else:
        return True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    i=x
    j=y
    R=(r+1)%4
    if R==0:
        i=x-1
    if R==1:
        j=y+1
    if R==2:
        i=x+1
    if R==3:
        j=y-1
    if i>Longueur-1:
        i=0
    if j>Hauteur-1:
        j=0
    if i<0:
        i=Longueur-1
    if j<0:
        j=Hauteur-1
    if Liste[j,i]==1:
        if random.randint(1,2)==1:
            r=(r+1)%4
        else:
            r=(r+3)%4
        h=h+1
        if h>4:
            Calcul=True
            m=0
            i=x
            j=y
            R=0
            while Calcul:
                m=m+1
                print(m)
                w=-m
                while w<=m and Calcul:
                    if R==0:
                        i=i-1
                    if R==1:
                        j=j+1
                    if R==2:
                        i=i+1
                    if R==3:
                        j=j-1
                    if i>0 and i<Longueur-1 and j>0 and j<Hauteur-1:
                        if Liste[j,i]==0:
                            Calcul=False
                    w=w+1
                R=(R+1)%4
            x=i
            y=j
            print(i,j)
    else:
        x=i
        y=j
        r=R
        h=0
        Liste[y,x]=1
    X=x*Taille
    Y=y*Taille
    pygame.draw.rect(screen, COULEUR, (X-l,Y-l,Taille,Taille), 0)                                     
        
    pygame.display.flip()
    
pygame.quit()
