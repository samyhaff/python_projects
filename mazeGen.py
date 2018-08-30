import random

dim = (5, 5)
dim_x, dim_y = dim

grid = [[0 for i in range(dim_x)] for j in range(dim_y)]
visited = [1]

    def valid(nb):
        y = nb % 4 - 1
        x = nb - (5 * y) - 1
        if x >= 0 and x <= dim_x - 1 and y >= 0 and y <= dim_y - 1:
            return True
        return False

    def list_moves(nb):
        moves = []
        nb = int(nb)
        if valid(nb + 5 * dim_y) and visited.count(nb + 5 * dim_y) < 1:
            moves.append(nb + 5 * dim_y)
        if valid(nb - 5 * dim_y) and visited.count(nb - 5 * dim_y) < 1:
            moves.append(nb - 5 * dim_y)
        if valid(nb + 1) and visited.count(nb + 1) < 1:
            moves.append(nb + 1)
        if valid(nb - 1) and visited.count(nb - 1) < 1:
            moves.append(nb - 1)
        return moves

# test
print(valid(1))
print(list_moves(1))

def gen():
    while len(list_moves((len(visited)) - 1)) == 0:
        visited.pop()
    next_visit = random.choice(list_moves(visited(len(visited) - 1)))
    visited.push(next_visit)

'''
while len(visited) != 25:
    gen()
    print(visited)
'''
