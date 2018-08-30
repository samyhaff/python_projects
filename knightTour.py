import time
import math

board = [[0 for i in range(8)] for j in range(8)]

def valid_move(x, y):
    if x >= 0 and x <= 7 and y >= 0 and y <= 7:
        return True
    return False

def result():
    if board.count(1) != 64:
        return False
    return True

def list_moves(x, y):
    valid = []
    if valid_move(x + 1, y + 2):
        valid.append([x + 1, y + 2])
    if valid_move(x - 1, y + 2):
        valid.append([x - 1, y + 2])
    if valid_move(x + 1, y - 2):
        valid.append([x + 1, y - 2])
    if valid_move(x - 1, y - 2):
        valid.append([x - 1, y - 2])
    if valid_move(x + 2, y - 1):
        valid.append([x + 2, y - 1])
    if valid_move(x + 2, y + 1):
        valid.append([x + 2, y + 1])
    if valid_move(x - 2, y - 1):
        valid.append([x - 2, y - 1])
    if valid_move(x - 2, y + 1):
        valid.append([x - 2, y + 1])
    return valid

visited = []
x = y = 0
def main():
    global visited
    global x
    global y
    if result:
        print(visited)
    else:
        print(list_moves(0, 0))


main()
