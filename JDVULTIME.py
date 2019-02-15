import math
import random
import pygame
import numpy as np
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

init = True
tailleCell = 10
width = 700
height = 500
hauteur = height // tailleCell
longueur = width // tailleCell
l = tailleCell // 2
pygame.init()

l1 = np.zeros([hauteur, longueur])
l2 = np.zeros([hauteur, longueur])

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Game of Life")
done = False
clock = pygame.time.Clock()
screen.fill(BLACK)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                if init == False:
                    init = True
                else:
                    init = False
            if event.key == K_ESCAPE:
                l1 = np.zeros([hauteur, longueur])
                l2 = np.zeros([hauteur, longueur])
                screen.fill(BLACK)
                init = True
        if init == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x = (event.pos[0] // tailleCell)
                y = (event.pos[1] // tailleCell)
                X = x * tailleCell
                Y = y * tailleCell
                l1[y, x]=(l1[y, x]+1)%2
                if l1[y, x]==0:
                    pygame.draw.rect(screen, BLACK, (X - l, Y - l,tailleCell, tailleCell), 0)
                else:
                    pygame.draw.rect(screen, GREEN, (X - l, Y - l,tailleCell, tailleCell), 0)

    if init == False:
        l2 = np.copy(l1)
        for y in range(1, hauteur - 1):
            for x in range(1, longueur - 1):
                voisines = 0
                for j in range(-1, 2):
                    for i in range(-1, 2):
                        if (l1[y + j, x + i] == 1):
                            if i != 0 or j != 0:
                                voisines = voisines + 1
                if (voisines < 2) or (voisines > 3):
                    l2[y,x] = 0
                if voisines == 3:
                    l2[y,x] = 1
                X = x * tailleCell
                Y = y * tailleCell
                if l2[y, x] == 0:
                    pygame.draw.rect(screen, BLACK, (X-l,Y-l,tailleCell,tailleCell), 0)
                else:
                    pygame.draw.rect(screen, GREEN, (X-l,Y-l,tailleCell,tailleCell), 0)
        l1 = np.copy(l2)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
