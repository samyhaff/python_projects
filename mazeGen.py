import random
import pygame
import time
import timeit

dim_x = 10
dim_y = 10

visited = [1]

def init_aff():
   pygame.init()
   size = (500,500)
   t = (size[0]/dim_x, size[1]/dim_y)
   screen = pygame.display.set_mode(size)
   screen.fill((255, 255, 255))
   pygame.display.set_caption("Maze")
   for y in range(dim_y):
      for x in range(dim_x):
         pygame.draw.rect(screen, (0,0,0), (x*int(t[1]),y*int(t[1]),int(t[0] - 3), int(t[1] - 3)), 0)
   pygame.display.flip()

init_aff()

def valid(nb):
    if nb >= 1 and nb <= dim_x * dim_y:
        return True
    return False

def list_moves(nb):
    moves = []
    nb = int(nb)
    if valid(nb + dim_y) and visited.count(nb + dim_y) < 1:
        moves.append(nb + dim_y)
    if valid(nb - dim_y) and visited.count(nb - dim_y) < 1:
        moves.append(nb - dim_y)
    if valid(nb + 1) and visited.count(nb + 1) < 1 and nb % dim_x != 0:
        moves.append(nb + 1)
    if valid(nb - 1) and visited.count(nb - 1) < 1 and nb % dim_x != 1:
        moves.append(nb - 1)
    return moves

def gen():
    pos = len(visited) - 1
    while len(list_moves(visited[pos])) < 1:
        pos -= 1
    next_visit = random.choice(list_moves(visited[pos]))
    visited.append(next_visit)

while len(visited) != dim_x * dim_y:
    gen()
print(visited)
