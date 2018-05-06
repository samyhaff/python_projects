import pygame
import numpy as np
import math
import random
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
width = 700
height = 700
hauteur = height // taille
longueur = width // taille
taille = 20
c = taille/2 #correction
x = 0
y = 0
xt = 0
yt = 0

board = np.zeros([longueur, hauteur])
board[x, y] = 1
move = []

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("A star PATH FINDING")
done = False
clock = pygame.time.Clock()
screen.fill(BLACK)

def canVisit(x):
    if x - 1 >= 1 and board[x - 1, y] == 0:
        move.append(0)
    if x + 1 <= longueur - 1 and board[x + 1, y] == 0:
        move.append(1)
    if y - 1 >= 1 and board[x, y - 1] == 0:
        move.append(2)
    if y + 1 <= hauteur - 1 and board[x, y + 1] == 0:
        move.append(3)

pygame.draw.rect(screen, GREEN, (x * taille, y * taille, taille, taille), 0)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if x > 1 and y > 1 and x < longueur - 2 and y < hauteur - 2:
        d = 3
    else:
        d = 2
    canVisit(x)
    rand = random.choice(move)
    moveSave = move[:]
    if rand == 0:
        xt = x - 1
        canVisit(xt)
        if len(move) >= d:
            x = xt
            pygame.draw.rect(screen, GREEN, (x * taille, y * taille, taille, taille), 0)
        else:
            moveSave.remove(0)
            rand = random.choice(moveSave)
    if rand == 1:
        xt = x + 1
        canVisit(xt)
        if len(move) >= d:
            x = xt
            pygame.draw.rect(screen, GREEN, (x * taille, y * taille, taille, taille), 0)
        else:
            moveSave.remove(1)
            rand = random.choice(moveSave)
    if rand == 2:
        yt = y - 1
        canVisit(xt)
        if len(move) >= d:
            y = yt
            pygame.draw.rect(screen, GREEN, (x * taille, y * taille, taille, taille), 0)
        else:
            moveSave.remove(2)
            rand = random.choice(moveSave)
    if rand == 3:
        yt = y + 1
        canVisit(xt)
        if len(move) >= d:
            y = yt
            pygame.draw.rect(screen, GREEN, (x * taille, y * taille, taille, taille), 0)
        else:
            print(moveSave)
            moveSave.remove(3)
            rand = random.choice(moveSave)
    move = []
    moveSave = []
    board[x, y] = 1
    pygame.display.flip()
    clock.tick(10)
pygame.quit()
