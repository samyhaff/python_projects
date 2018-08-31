import random
import turtle

import turtle
loadWindow = turtle.Screen()
turtle.speed(1)
turtle.colormode(255)
turtle.pensize(1)

dim_x = 500
dim_y = 500

grid = [[0 for i in range(dim_x)] for j in range(dim_y)]

path = [1]
visited = [1]

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
    while len(list_moves(path[len(path) - 1])) < 1:
        path.pop()
    next_visit = random.choice(list_moves(path[len(path) - 1]))
    path.append(next_visit)

while len(path) != dim_x * dim_y:
    gen()
print(path)
