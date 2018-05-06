import math
import random
import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

size = (500, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("The Game of Life")
 
done = False

clock = pygame.time.Clock()
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            print("Zone dangereuse")
    screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
