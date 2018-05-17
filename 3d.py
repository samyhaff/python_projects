from Fonctions import*
import math
import random
import pygame
import numpy as np
from pygame.locals import *

#---------#
#Variables#
#---------#

#Bases#

Repère=["x","y","z"]
EcranAtt={"Hauteur":700,"Longueur":700}
ChampDeVision={"Horizontal":180,"Vertical":90}

#Espace#

Hauteur=100
Profondeur=100
Longueur=100
Espace=[[[None]*Longueur]*Hauteur]*Profondeur
Milieu=[Longueur//2,Hauteur//2,Profondeur//2]
PDV=[Longueur//2,Hauteur//2,0]

#Couleurs#

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

COULEUR=GREEN
FOND=BLACK

#---------#
#Fonctions#
#---------#

#Secondaires#

def ColorierFace(x,y,z,Z,Couleur):
    global Espace
    for j in range(y,Y):
        for i in range(x,X):
            Espace[z][j][i]=Couleur
            

def VoirLigne(Ligne):
    i=0
    while i<len(Ligne) and Ligne[i]==0:
        i+=1
    return Ligne[i]

def AssemblerLigne(Ligne):
    i=0
    while i<len(Ligne) and Ligne[i]==0:
        i+=1
    return Ligne[i]

def SuivreRayon1(Position,i,j,Alpha,Beta,Espace):
    z=Position[0]
    y=Position[1]
    x=Position[2]
    BoolCouleur=False
    if i!=0:
        f=i/abs(i)
    else:
        f=0
    if j!=0:
        g=j/abs(j)
    else:
        g=0
    while Espace[z][y][x]==None:
        while Contact(x,y,z,Beta,j) and Espace[z][y][x]==None:
            y+=g
        y-=g
        while Contact(x,y,z,Alpha,i) and Espace[z][y][x]==None:
            x+=f
        x-=f
        z+=1
    return Espace[z][y][x]

def Contact(x,y,Alpha,i):
    Angle=i*tan(Alpha)
    Y1=(X-0,5)*Angle
    Y1=int(Y1)
    Y2=(X+0,5)*Angle
    Y2=int(Y2+1)
    if Y1<y<Y2:
        return True
    else:
        return False

def Quadriller(Espace,Couleur,Distance):
    for z in range(0,len(Espace),Distance):
        for y in range(0,len(Espace[z]),Distance):
            for x in range(0,len(Espace[z][y]),Distance):
                Espace[z][y][x]=Couleur
    return Espace

#Main#

def Fabriquer(Espace,Position,Direction):
    Ecran=[[None]*EcranAtt["Longueur"]]*EcranAtt["Longueur"]
    Alpha=ChampDeVision["Horizontal"]/EcranAtt["Longueur"]
    Beta=ChampDeVision["Vertical"]/EcranAtt["Hauteur"]
    Quadriller(Espace,RED,10)
    Coeffs={}
    #Coeff["Horizontal"]=1/cos(Alpha)
    #Coeff["Vertical"]=1/cos(Beta)
    h=EcranAtt["Hauteur"]
    l=EcranAtt["Longueur"]
    h1=-h//2
    h2=h//2
    l1=-l//2
    l2=l//2
    for j in range(h1,h2):
        for i in range(l1,l2):
            Ecran[j+h2][i+l2]=SuivreRayon1(Position,i,j,Alpha,Beta,Espace)
    return Ecran




            
#---------#
#Fonctions#
#---------#    

Ecran=Fabriquer(Espace,PDV,Milieu)

pygame.init()
size=(EcranAtt["Longueur"],EcranAtt["Hauteur"])
screen = pygame.display.set_mode(size)
pygame.display.set_caption("something")
clock = pygame.time.Clock()
screen.fill(FOND)
for y in range(len(Ecran)):
    for x in range(len(Ecran[y])):
        pygame.draw.rect(screen, Ecran[y][x], (x,y,5,5), 0)
pygame.display.flip()
clock.tick(1000000)
pygame.quit()

    
