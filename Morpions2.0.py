import math
import random
import pygame
import numpy as np
from pygame.locals import *
pygame.init()

Width=700
Height=700
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
FOND=WHITE

size=(Width,Height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Morpions")
clock = pygame.time.Clock()
screen.fill(FOND)

def AffichageDuPauvre():
    for g in range(0,3):
        print(L[3*g],L[3*g+1],L[3*g+2])

def Interactions():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game = False
                Victory=False
            if event.type==pygame.K_LEFT and x>0:
                x=x-1
            if event.type==pygame.K_RIGHT and x<2:
                x=x+1
            if event.type==pygame.K_UP and y>0:
                y=y-1
            if event.type==pygame.K_DOWN and y<2:
                y=y+1
            if event.type==pygame.K_RETURN:
                Jouer=True

def MoveOrdinateur():
    

def GameTest():
    global Game
    v=0
    for i in range(0,9):
        if L[i]=="X" or L[i]=="O":
            v=v+1
    if v==9:
        game=False

#Initialisation
L=["a"]*9
Game=True
Jouer=False
if True!=True:
    Joueur1=input("Joueur1:")
    Joueur2=input("Joueur2:")
Joueur1="Humain"
Joueur2="Humain"
Joueur=0
#Fin Initialisation

while Game:
    if Joueur==0:
        if Joueur1=="Ordinateur":
            Jouer=True
        else:
                Interactions()
                if Jouer:
                    Placer()
    else:
        if Joueur2=="Ordinateur":
            Jouer=True
        else:
                Interactions()
                if Jouer:
                    Placer()
    WinTest()
    GameTest()
    Joueur=(Joueur+1)%2
    Jouer=False
    
    
    
        



        
    pygame.display.flip()
    clock.tick(1000)
pygame.quit()
