from Fonctions import*
import math

#---------#
#Variables#
#---------#

#Bases#

Repère=["x","y","z"]
Ecran={"Hauteur":10,"Longueur":10}
ChampDeVision={"Horizontal":180,"Vertical":90]

#Espace#

Hauteur=10
Profondeur=10
Longueur=10
Espace=[[[Noir]*Longueur]*Hauteur]*Profondeur
Milieu=[Longueur//2,Hauteur//2,Profondeur//2]

#Couleurs#

Bleu=[0,0,255]
Vert=[0,255,0]
Rouge=[255,0,0]
Noir=[0,0,0]
Blanc=[255,255,255]

#---------#
#Fonctions#
#---------#

#Secondaires#

def ColorierFace(x,y,z,Z,y,Couleur):
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

#Main#

def Voir(Structure,Position,Direction):
    global Espace
    Ecran=[[Noir]*Ecran["Longueur"]]*Ecran["Longueur"]
    Alpha=ChampDeVision["Horizontal"]/Ecran["Longueur"]
    Beta=ChampDeVision["Vertical"]/Ecran["Hauteur"]
    Coeffs={}
    Coeff["Horizontal"]=1/cos(Alpha)
    Coeff["Vertical"]=1/cos(Beta)
    for y in range(Ecran["Hauteur"]):
        for x in range(Ecran["Longueur"]):
            Ecran[y][x]=VoirLigne(AssemblerLigne(x,y,Alpha,Beta))
    return Ecran
    
    
