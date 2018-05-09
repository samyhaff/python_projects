import math
import pygame
import numpy as np
from pygame.locals import *

def Progression(V,D,F):
    pygame.init()
    done=False
    
    Width=500
    Height=20

    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)
    GREEN    = (   0, 255,   0)
    RED      = ( 255,   0,   0)
    BLUE     = (   0,   0, 255)

    COULEUR=GREEN
    FOND=BLACK

    size=(Width,Height)
    screen = pygame.display.set_mode(size)
     
    pygame.display.set_caption("Progression")
    clock = pygame.time.Clock()
    screen.fill(FOND)
    
    E=(Width*V)//(F-D)
    
    pygame.draw.rect(screen, COULEUR, (0,0,E,Height),0)
    pygame.display.flip()
    clock.tick(1000000)
    if V>=F or done:
        pygame.quit()


        
