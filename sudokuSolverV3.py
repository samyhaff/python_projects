grille = [[3,0,6,5,0,8,4,0,0],
        [5,2,0,0,0,0,0,0,0],
        [0,8,7,0,0,0,0,3,1],
        [0,0,3,0,1,0,0,8,0],
        [9,0,0,8,6,3,0,0,5],
        [0,5,0,0,9,0,6,0,0],
        [1,3,0,0,0,0,2,5,0],
        [0,0,0,0,0,0,0,7,4],
        [0,0,5,2,0,6,3,0,0]]

e = [0, 0]

def vLine(i, test,board):
    for j in range(9):
        if board[i][j] == test:
            return True
    return False

def vColumn(j, test,board):
    for i in range(9):
        if board[i][j] == test:
            return True
    return False

def vBlock(i, j, test,board):
    for I in range(3):
        for J in range(3):
            if(board[i//3+I][j//3 + J] == test):
                return True
    return False

def validMove(i, j, test,board):
    if vColumn(j, test,board) == False and vBlock(i, j, test,board) == False and vLine(i, test,board) == False:
        return True
    else:
        return False


def next(board):
    Liste=[0]*2
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                Liste[0] = i
                Liste[1] = j
    return Liste

def checkEmpty(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                return True
    return False

def solve(board):
    if checkEmpty(board) == False:
        return True
    else:
        e = next(board)
        i = e[0]
        j = e[1]
        for k in range(1, 10):
            aff(board)
            if validMove(i, j, k, board) == True:
                board[i][j] = k
                if solve(board) == True:
                    return True
                #board[i][j] = 0
        return False

def aff(board):
    for i in range(0,9):
        print(board[i])
    print("")

if solve(grille):
    print("solved!")
else:
    print("No solution exists")
