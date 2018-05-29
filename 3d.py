#------------#
#Importations#
#------------#


from Fonctions import*
import math
import random
import pygame
import numpy as np
from pygame.locals import *
from math import*
import copy
import time

#---------#
#Variables#
#---------#

#Bases#

T=50

Repère=["x","y","z"]

EcranAtt={"Longueur":1440,"Hauteur":700}
VisionAtt={"Horizontal":140,"Vertical":80} #180,90
EspaceAtt={"Longueur":T,"Hauteur":T,"Profondeur":T}

#Espace#

L=EspaceAtt["Longueur"]
H=EspaceAtt["Hauteur"]
P=EspaceAtt["Profondeur"]

#Positions#

Milieu=[L//2,H//2,P//2]
P1=[L//2+80,H//2-6,0]
P5=[L//2+8,H//2-6,0]
P2=[350,150,250]
P3=[3,1,2]
P4=[35,15,25]

#Couleurs#

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW   = ( 255, 255,   0)

COULEUR=GREEN
FOND=BLACK

#---------#
#Fonctions#
#---------#

#Echecs#

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

def SuivreRayon(Espace,Position,Alpha,Beta,Précision=0.1):
    s=float(0)
    p=Précision
    P=Position[:]
    x=P[0]
    y=P[1]
    z=P[2]
    Alpha=math.radians(Alpha)
    Beta=math.radians(Beta)
    Bool=True
    while Espace[z][y][x]==None and Bool:
        s+=p
        x=P[0]+int(s*math.sin(Alpha))
        y=P[1]+int(s*math.sin(Beta))
        z=P[2]+int(s*math.cos(Alpha))
        Bool=InEspace(Espace,x,y,z)
    #print(x,y,z,Bool)
    if Bool:
        return Espace[z][y][x]
    else:
        return None

def InEspace(Espace,x,y,z):
    Bool=True
    if x<0 or x>=len(Espace[0][0])-1:
        Bool=False
    if y<0 or y>=len(Espace[0])-1:
        Bool=False
    if z<0 or z>=len(Espace)-1:
        Bool=False
    return Bool
        

def Plaquer(Espace,Plan,Dimension,Valeur):
    V=Valeur
    D=Dimension
    for j in range(len(Plan)):
        for i in range(len(Plan[j])):
            if D=="z":
                Espace[V][j][i]=Plan[j][i]
            if D=="y":
                Espace[j][V][i]=Plan[j][i]
            if D=="x":
                Espace[j][i][V]=Plan[j][i]
            #print(i,j,V,len(Plan),len(Plan[0]),len(Espace),len(Espace[0]))
    return Espace

def ContourD2(Espace,Couleur):
    l=len(Espace[0][0])
    h=len(Espace[0])
    p=len(Espace)
    Plan=Dimensionner([h,p])
    Plan=ContourD1(Plan,Couleur)
    Espace=Plaquer(Espace,Plan,"x",0)
    Espace=Plaquer(Espace,Plan,"x",l-1)
    Plan=Dimensionner([l,p])
    Plan=ContourD1(Plan,Couleur)
    Espace=Plaquer(Espace,Plan,"y",0)
    Espace=Plaquer(Espace,Plan,"y",h-1)
    return Espace
    

def Insérer(Espace,Objet,Coordonnées):
    L1=len(Objet[0][0])
    H1=len(Objet[0])
    P1=len(Objet)
    C=Coordonnées[:]
    k2=-P1//2+C[2]
    k1=-H1//2+C[1]
    k0=-L1//2+C[0]
    for P in range(P1):
        for H in range(H1):
            for L in range(L1):
                p=P+k2
                h=H+k1
                l=L+k0
                Espace[p][h][l]=Objet[P][H][L]
    return Espace


def ContourD1(Plan,Couleur):
    l1=len(Plan[0])
    l2=len(Plan)
    for i in range(l1):
        Plan[0][i]=Couleur
        Plan[l2-1][i]=Couleur
    for j in range(l2):
        Plan[j][0]=Couleur
        Plan[j][l1-1]=Couleur
    return Plan

def Face(Espace,Ecran):
    L=len(Espace[0][0])
    H=len(Espace[0])
    P=len(Espace)
    for Z in range(0,P):
        for Y in range(0,H):
            for X in range(0,L):
                K=P-Z-1
                if Espace[K][Y][X]!=None:
                    Ecran[Y][X]=Espace[K][Y][X]
    return Ecran

def Elargir(Liste,Facteur=2):
    Sortie=[]
    for i in Liste:
        for d in range(Facteur):
            Sortie.append(i)
    return Sortie


def Agrandir(Espace,Facteur):
    h=len(Espace[0])
    p=len(Espace)
    for k in range(p):
        for j in range(h):
            Espace[k][j]=Elargir(Espace[k][j],Facteur)
    for k in range(p):
        Espace[k]=Elargir(Espace[k],Facteur)
    Espace=Elargir(Espace,Facteur)
    return Espace
    
def Dimensionner(Attributs,Valeur=None):
    Type=type(Attributs)
    if Type==dict:
        Liste=list(Attributs.values())
    elif Type==list:
        Liste=Attributs
    else:
        Erreurs("Dimensionner")
        return None
    if len(Liste)==2:
        Objet=[[Valeur for i in range(Liste[0])] for j in range(Liste[1])]
    if len(Liste)==3:
        Objet=[[[Valeur for i in range(Liste[0])] for j in range(Liste[1])] for k in range(Liste[2])]
    return Objet

def Contact(x,y,Alpha,i):
    Angle=i*math.tan(Alpha)
    Y1=int(float(x-0.5)*Angle)
    Y2=int(float(x+0.5)*Angle)
    if Y1<y<Y2:
        return True
    else:
        return False

def Substract(liste1,liste2):
    l=len(liste1)
    liste=[0]*l
    for i in range(l):
        liste[i]=liste1[i]-liste2[i]
    return liste

def Quadriller(Espace,EspaceAtt,D):
    L=len(Espace[0][0])
    H=len(Espace[0])
    P=len(Espace)
    for Z in range(0,P,D):
        for Y in range(0,H,D):
            for X in range(0,L,D):
                Espace[Z][Y][X]=((255*Z)//P,255,0)
    return Espace

#Main#

def Fabriquer(Espace,Ecran,VisionAtt,Départ,Destination,Précision):
    p=Précision
    L=len(Espace[0][0])
    H=len(Espace[0])
    P=len(Espace)
    l=len(Ecran[0])
    h=len(Ecran)
    Hl=VisionAtt["Horizontal"]
    Vl=VisionAtt["Vertical"]
    Alpha=float(Hl/l)
    Beta=float(Vl/h)
    Coeffs={}
    #Coeff["Horizontal"]=1/cos(Alpha)
    #Coeff["Vertical"]=1/cos(Beta)
    u=[1,0,0]
    v=[0,0,1]
    Trajectoire=Substract(Destination,Départ)
    A0=Angle(u,Trajectoire)
    B0=Angle(v,Trajectoire)
    A0=0
    B0=0
    A1=int(-Hl//2+A0)
    A2=int(Hl//2+A0)
    B1=int(-Vl//2+B0)
    B2=int(Vl//2+B0)
    t=time.time()
    for J in range(h):
        for I in range(l):
            j=int((J-h//2)*Beta+B0)
            i=int((I-l//2)*Alpha+A0)
            Ecran[J][I]=SuivreRayon(Espace,Départ,i,j,p)
        #Progression(J,0,h)
        Show(str(int(TempsRestant(J,0,h,t,time.time()))),70)
        #print(TempsRestant(J,0,h,t,time.time()))
    Show(str(TempsRestant(J,0,h,t,time.time())),70,False)
    return Ecran

def RemplacerDansPlan(Ecran,Old,New):
    h=len(Ecran)
    l=len(Ecran[0])
    for j in range(h):
        for i in range(l):
            if Ecran[j][i]==Old:
                Ecran[j][i]=New
    return Ecran

def RemplacerDansEspace(Ecran,Old,New):
    p=len(Ecran)
    h=len(Ecran[0])
    l=len(Ecran[0][0])
    for z in range(p):
        for y in range(h):
            for x in range(l):
                if Ecran[z][y][x]==Old:
                    Ecran[z][y][x]=New
    return Ecran

def Visualiser(Ecran):
    pygame.init()
    l=len(Ecran[0])
    h=len(Ecran)
    screen = pygame.display.set_mode((l,h))
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

def n(Vecteur):
    return sqrt(sum([Grandeur**2 for Grandeur in Vecteur]))


def Angle(Vecteur1,Vecteur2):
    V1=Vecteur1
    V2=Vecteur2
    V1x=V1[0]
    V1y=V1[1]
    V2x=V2[0]
    V2y=V2[1]
    try:
        Angle=acos(V1x*V2x+V1y*V2y)/(n(V1)*n(V2))
        return Angle
    except:
        return 0
                  
#Principales#

def Main():
    print("Création de l'Espace")
    Espace=Dimensionner(EspaceAtt)
    Cube=Dimensionner(P4)
    #Cube=Agrandir(Cube,2)

    print("Création de l'Ecran")
    Ecran=Dimensionner(EcranAtt)


    print("Création du Cube")
    #Espace=Quadriller(Espace,23)
    Cube=ContourD2(Cube,RED)
    #RemplacerDansEspace(Cube,None,YELLOW)

    print("Insertion du Cube")
    Espace=Insérer(Espace,Cube,Milieu)

    print("Fabrication de l'Image")
    Ecran=Fabriquer(Espace,Ecran,VisionAtt,P5,Milieu,1)
    #Ecran=Face(Espace,Ecran)
    Ecran=RemplacerDansPlan(Ecran,None,FOND)

    print("Visualisation de l'Image")
    Visualiser(Ecran)

#-------#
#Actions#
#-------#


