#NombreDeTests

Tests=1000


#Programme à Tester

from SudokuMarc import*

def Programme():
    Soluce=Permuter(Sudoku)
    TheOne=Vider(Soluce)
    Main(TheOne)



#Testeur

from Progression import*
import math
import random
import pygame
import numpy as np
from pygame.locals import *
pygame.init()

done=False

Test=1
while Test<Tests and not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_RETURN or event.key == K_ESCAPE:
                done=True
    Test=Test+1
    try:
        Programme()
        Progression(Test,0,Tests)
    except:
        print("Il y a eu une erreur à l'essai",Test,".")

pygame.quit()
