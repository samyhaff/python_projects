import random

board = [[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 2, 0, 0],
        [0, 0, 1, 2, 1, 0, 0],
        [0, 1, 1, 2, 2, 0, 0],
        [0, 2, 1, 2, 1, 0, 0]]

def checkMove(x, y):
    Y = 5 - y
    if (0 <= x) and (x < 6):
        if (Y == 0) or (Y - 1) != 0:
            return True
    return False

def win(x, y):
    # i = ligne
    # j = colonne

    # test lignes
    test = []
    for i in range(0, 6):
        for j in range(0, 7):
            if len(test) != 7:
                test.append(str(board[i][j]))
            else:
                chaine = "".join(test)
                if "2222" in chaine:
                    win = "IA"
                    return True
                elif "1111" in chaine:
                    win = "joueur"
                    return True
                test = []
                chaine = ""

    # test colonnes
    test = []
    for j in range(0, 7):
        for i in range(0, 6):
            if len(test) != 6:
                test.append(str(board[i][j]))
            else:
                chaine = "".join(test)
                if "2222" in chaine:
                    win = "IA"
                    return True
                elif "1111" in chaine:
                    win = "joueur"
                    return True
                test = []
                chaine = ""

    # test diagonales
    val = board[x][y]
    testx = x
    testy = y
    compteur = 1
    diagonale = []
    while checkMove(testx, testy) == True:
        testx = testx - 1
        testy = testy - 1
        if board[testx][testy] == val:
            compteur = compteur + 1
        else:
            break
    if compteur != 4:
        compteur = 1
        while checkMove(testx, testy) == True:
            testx = testx + 1
            testy = testy + 1
            if board[testx][testy] == val:
                compteur = compteur + 1
            else:
                break

    if compteur == 4:
        if val == 1:
            win = "joueur"
            return True
        if val == 2:
            win = "IA"
            return True
    compteur = 1

    return False

    """

    for i in range(0, 6):
        for j in range(0, 7):

            if board[i][j] != 0:
                val = board[i][j]
                compteur = 1

                for t in range(1, 4):
                    if checkMove(i - t, j - t) == True:
                        if board[i - t][j - t] == val:
                            compteur = compteur + 1

                if compteur == 4:
                    if val == 1:
                        win = "joueur"
                    else:
                        win = "IA"
                    return True
                else:
                    compteur = 1

                for k in range(1, 4):
                    if checkMove(i + k, j + k) == True:
                        print(i)
                        print(j)
                        if board[i + k][j + k] == val:
                            compteur = compteur + 1

                if compteur == 4:
                    if val == 1:
                        win = "joueur"
                    else:
                        win = "IA"
                    return True
                else:
                    compteur = 1

    """

# test
if win(1, 4) == True:
    print("test reussi")
else:
    print("TOZ")

"""

while win() == False:
    # tour joueur
    x = int(input("X: "))
    y = int(input("Y: "))
    grid[x][y] = 1
    while checkMove(x, y) == False or board[x][y] != 0:
        grid[x][y] = 0
        x = int(input("X: "))
        y = int(input("Y: "))
        grid[x][y] = 1

    # tour IA
    x = random.randint(0, 6)
    y = random.randint(0, 5)
    grid[x][y] = 2
    while checkMove(x, y) == False or board[x][y] != 0:
        grid[x][y] = 0
        x = random.randint(0, 6)
        y = random.randint(0, 5)
        grid[x][y] = 2

"""
