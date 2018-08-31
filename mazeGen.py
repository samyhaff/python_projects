import random

dim_x = 5
dim_y = 5

grid = [[0 for i in range(dim_x)] for j in range(dim_y)]
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
    pos = len(visited) - 1
    while len(list_moves(visited[pos])) < 1:
        pos -= 1
    next_visit = random.choice(list_moves(visited[pos]))
    visited.append(next_visit)

while len(visited) != dim_x * dim_y:
    gen()
print(visited)
