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
T=20

Hauteur=T
Profondeur=T
Longueur=T
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
    x=Position[0]
    y=Position[1]
    z=Position[2]+1
    BoolCouleur=False
    if i!=0:
        f=int(i/abs(i))
    else:
        f=0
    if j!=0:
        g=int(j/abs(j))
    else:
        g=0
    Recherche=True
    try:
        while Recherche:
            while Espace[z][y][x]==None and Contact(z,y,Beta,j):
                y+=g
            if Espace[z][y][x]!=None:
                return Espace[z][y][x]
            else:
                y-=g
                while Espace[z][y][x]==None and Contact(z,x,Alpha,i):
                    x+=f
                if Espace[z][y][x]!=None:
                    return Espace[z][y][x]
                else:
                    x-=f
                    z+=1
    except:
        return FOND

def SuivreRayon(P,i,j,Alpha,Beta,Espace):
    try:
        suivi=0
        while Espace[z][y][x]==None:
            suivi+=0.1
            x=P[0]+int(suivi/math.sin(float(i)*Alpha))
            y=P[1]+int(suivi/math.sin(float(j)*Beta))
            z=P[2]+int(suivi/math.cos(float(i)*Alpha))
        print(Espace[z][y][x])
        return Espace[z][y][x]
    except:
        return FOND


def Contact(x,y,Alpha,i):
    Angle=i*math.tan(Alpha)
    Y1=int(float(x-0.5)*Angle)
    Y2=int(float(x+0.5)*Angle)
    if Y1<y<Y2:
        return True
    else:
        return False

def Quadriller(Espace,Couleur,Distance):
    for z in range(0,Profondeur):
        for y in range(0,Hauteur):
            for x in range(0,Longueur,Distance):
                Espace[z][y][x]=RED
    return Espace

#Main#

def Fabriquer(Espace,Position,Direction):
    Ecran = [[None for i in range(EcranAtt["Longueur"])] for i in range(EcranAtt["Hauteur"])]
    Alpha=ChampDeVision["Horizontal"]/EcranAtt["Longueur"]
    Beta=ChampDeVision["Vertical"]/EcranAtt["Hauteur"]
    Espace=Quadriller(Espace,RED,6)
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
            Ecran[j+h2][i+l2]=SuivreRayon(Position,i,j,Alpha,Beta,Espace)
    return Ecran




            
#---------#
#Fonctions#
#---------#

#Espace=[[[None]*3]*3]*3

Espace = [[[None for i in range(Longueur)] for i in range(Hauteur)] for i in range(Profondeur)]

print("Fabrication en cours")
Ecran=Fabriquer(Espace,PDV,Milieu)

print("Visualisation en cours")
pygame.init()
screen = pygame.display.set_mode((EcranAtt["Longueur"],EcranAtt["Hauteur"]))
pygame.display.set_caption("3 Dimensions")
screen.fill(FOND)
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for y in range(len(Ecran)):
        for x in range(len(Ecran[y])):
            screen.fill(Ecran[y][x], ((x,y), (1, 1)))
    pygame.display.flip()
pygame.quit()

#            pygame.draw.rect(screen, Ecran[y][x], (x,y,1,1), 0)    
