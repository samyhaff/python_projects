board = [[3,0,6,5,0,8,4,0,0],
        [5,2,0,0,0,0,0,0,0],
        [0,8,7,0,0,0,0,3,1],
        [0,0,3,0,1,0,0,8,0],
        [9,0,0,8,6,3,0,0,5],
        [0,5,0,0,9,0,6,0,0],
        [1,3,0,0,0,0,2,5,0],
        [0,0,0,0,0,0,0,7,4],
        [0,0,5,2,0,6,3,0,0]]

e = [0, 0]

def vLine(i, test):
    for j in range(9):
        if board[i][j] == test:
            return True
    return False

def vColumn(j, test):
    for i in range(9):
        if board[i][j] == test:
            return True
    return False

def vBlock(i, j, test):
    for I in range(3):
        for J in range(3):
            if(board[i//3+I][j//3 + J] == test): # this way it cecks the blocks correctly 
                # if you input 2,2,9 it checks 2//3+range == 0+0-3 
                return True
    return False

def validMove(i, j, test):
    if vColumn(j, test) == False and vBlock(i, j, test) == False and vLine(i, test) == False:
        return True
    else:
        return False

def checkEmpty():
    global e
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                e[0] = i
                e[1] = j
                return True
    return False

def solve():
    global e
    if checkEmpty() == False:
        return True
    i = e[0]
    j = e[1]
    for k in range(1, 10): 
        if validMove(i, j, k) == True:
            board[i][j] = k
            if solve() == True:
                return True
            board[i][j] = 0
    return False

printBoard()

if solve():
    print("solved!")
else:
    print("No solution exists")

def printBoard():
    for i in range(9):
        for j in range(9):
            print(board[i][j])
        print ('\n')



   
        
        






    
