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

Width = 1440
Height = 800
Taille = 10

Longueur=Width//Taille
Hauteur=Height//Taille
l = Taille//2

Grille = np.zeros([Hauteur, Longueur])

screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Maze Serpent")
done = False
clock = pygame.time.Clock()
screen.fill(FOND)

x=0
y=0
r=0
Grille[y,x]=1

i=x
j=y
Voisine=0

X=x*Taille
Y=y*Taille
pygame.draw.rect(screen, COULEUR, (X-l,Y-l,Taille,Taille), 0)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    Liste=[0,1,3]
    Sortie=[]
    for a in range(0,3):
        Random=random.randint(0,2-a)
        Sortie.append(Liste[Random])
        del Liste[Random]
    Liste=Sortie[:]
    Recherche=True

    if Recherche:
        i=x
        j=y
        R=(r+Liste[0])%4
        if R==0:
            i=x-2
        if R==1:
            j=y-2
        if R==2:
            i=x+2
        if R==3:
            j=y+2
        if i>=0 and i<=Longueur-1 and j>=0 and j<=Hauteur-1:
            Voisine=0
            for e in range(-1,2):
                for d in range(-1,2):
                    if d+i>=0 and d+i<=Longueur-1 and e+j>=0 and e+j<=Hauteur-1:
                        if Grille[e+j,d+i]==1:
                            Voisine+=1
            if Voisine<=2:
                Recherche=False

    if Recherche:
        i=x
        j=y
        R=(r+Liste[1])%4
        if R==0:
            i=x-2
        if R==1:
            j=y-2
        if R==2:
            i=x+2
        if R==3:
            j=y+2
        if i>=0 and i<=Longueur-1 and j>=0 and j<=Hauteur-1:
            Voisine=0
            for e in range(-1,2):
                for d in range(-1,2):
                    if d+i>=0 and d+i<=Longueur-1 and e+j>=0 and e+j<=Hauteur-1:
                        if Grille[e+j,d+i]==1:
                            Voisine+=1
            if Voisine<=2:
                Recherche=False
    if Recherche:
        i=x
        j=y
        R=(r+Liste[2])%4
        if R==0:
            i=x-2
        if R==1:
            j=y-2
        if R==2:
            i=x+2
        if R==3:
            j=y+2
        if i>=0 and i<=Longueur-1 and j>=0 and j<=Hauteur-1:
            Voisine=0
            for e in range(-1,2):
                for d in range(-1,2):
                    if d+i>=0 and d+i<=Longueur-1 and e+j>=0 and e+j<=Hauteur-1:
                        if Grille[e+j,d+i]==1:
                            Voisine+=1
            if Voisine<=2:
                Recherche=False
                
    if Recherche:
        i=x
        j=y
        R=(r+1)%4
        Calcul=True
        if Calcul:
            i=x
            j=y
            if R==0:
                i=x-1
            if R==1:
                j=y-1
            if R==2:
                i=x+1
            if R==3:
                j=y+1
            if i>=0 and i<=Longueur-1 and j>=0 and j<=Hauteur-1:
                if Grille[j,i]==1:
                    x=i
                    y=j
                    r=R
                    Calcul=False
        if Calcul:
            i=x
            j=y
            if r==0:
                i=x-1
            if r==1:
                j=y-1
            if r==2:
                i=x+1
            if r==3:
                j=y+1
            if i>=0 and i<=Longueur-1 and j>=0 and j<=Hauteur-1:
                if Grille[j,i]==1:
                    x=i
                    y=j
                    Calcul=False
            
        if Calcul:
            i=x
            j=y
            r=(r+3)%4
            Calcul=False

        if i>=0 and i<=Longueur-1 and j>=0 and j<=Hauteur-1:
            Voisine=0
            for e in range(-1,2):
                for d in range(-1,2):
                    if d+i>=0 and d+i<=Longueur-1 and e+j>=0 and e+j<=Hauteur-1:
                        if Grille[e+j,d+i]==1:
                            Voisine+=1
            if Voisine<=2:
                Recherche=False
            else:
                pygame.draw.rect(screen, RED, (X-l,Y-l,Taille,Taille), 0) 

    if Recherche==False:
        f=(i+x)//2
        g=(j+y)/2
        x=i
        y=j
        r=R
        Grille[y,x]=1
        X=x*Taille
        Y=y*Taille
        pygame.draw.rect(screen, COULEUR, (x*Taille-l,y*Taille-l,Taille,Taille), 0)
        pygame.draw.rect(screen, COULEUR, (((i+x)//2)*Taille-l,((j+y)//2)*Taille-l,Taille,Taille), 0) 
    pygame.display.flip()
    clock.tick(10000)
pygame.quit()


# si droite
#    droite
#    tourne droite
#sinon
#    si avant
#        avant
#    sinon
#        tourne gauche
