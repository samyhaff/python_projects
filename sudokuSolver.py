import random
import numpy

grid = [[8,1,2,7,5,3,6,4,9],
        [9,4,3,6,8,2,1,7,5],
        [6,7,5,4,9,1,2,8,3],
        [1,5,4,2,3,7,8,9,6],
        [3,6,9,8,4,5,7,2,1],
        [2,8,7,1,6,9,5,3,4],
        [5,2,1,9,7,4,3,6,8],
        [4,3,8,5,2,6,9,0,7],
        [7,9,6,3,1,8,4,0,2]]

def createFromString(chaine):
    chaines = chaine.split()
    grid=[list(map(int,chaines[i])) for i in range(len(chaines))]
    return grid

def valid(i, j, v):
    if grid[i].count(v) > 0:
        return False
    if [row[j] for row in grid].count(v) > 0:
        return False
    i_ = i // 3
    j_ = j // 3
    for x in range(3 * i_, 3 * (i_ + 1)):
        for y in range(3 * j_, 3 * (j_ + 1)):
            if grid[x][y] == v:
                return False
    return True

def giveEmptyLoc(grid):
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return [x, y]
    return False

def backtrack(grid):
    if not giveEmptyLoc(grid):
        return True
    for v in range(1, 10):
        i, j = giveEmptyLoc(grid)
        if valid(i, j, v):
            grid[i][j] = v
            if backtrack(grid):
                return True
            grid[i][j] = 0
    return False

if __name__ == "__main__":
    if backtrack(grid):
        for row in grid:
            print(" ".join(map(str,row)))
    else:
        print("unsolvable grid")
