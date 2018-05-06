import random
import math
import tkinter

IA = False
Entrée=["g","h","d","b"]
Random = 1

board3 = [0, 0, 0, 0, #testSpawn
          0, 0, 0, 0,
          0, 0, 0, 0,
          0, 0, 0, 0]

board2 = [0, 0, 0, 0, #testGameOver
          0, 0, 1, 0,
          0, 0, 0, 0,
          0, 0, 0, 0]

board = [0, 0, 0, 0, #Affichage
         0, 0, 0, 0,
         0, 0, 0, 0,
         0, 0, 0, 0]

# indices
# [0, 1, 2, 3
#  4, 5, 6, 7
#  8, 9, 10, 11
#  12, 13, 14, 15]

def move():
    for x in range(0, 4):
        décale1 = []
        décale2 = []
        for y in range(0, 4):
            if (m == "h") or (m == "b"):
                i = x + 4 * y
            if (m == "g") or (m == "d"):
                i = y + 4 * x
            décale1.append(board[i])
        if (m == "b") or (m == "d"): #reverse
            décale1.reverse()
        for i in range(0, 4):
            if décale1[i] != 0:
                décale2.append(décale1[i])
        nb = len(décale2)
        for i in range(0, nb - 1):
            if décale2[i] == décale2[i+1]:
                décale2[i] = 2 * décale2[i]
                décale2[i+1] = 0
        for j in range(0, nb - 1):
            if décale2[j] == 0:
                del décale2[j]
        décale3 = décale2 + (4 - len(décale2)) * [0]
        if (m == "b") or (m == "d"):
            décale3.reverse()
        for y in range(0, 4):
            if (m == "h") or (m == "b"):
                i = x + 4 * y
            if (m == "g") or (m == "d"):
                i = y + 4 * x
            board[i] = décale3[y]

def gen():
    indices = []
    for i in range(0, 15):
        if board[i] == 0:
            indices.append(i)
    Random = random.randint(0, len(indices) - 1)
    board[Random] = 2 * random.randint(1, 2)

def affichage():
    print(board[0],"|", board[1],"|", board[2],"|", board[3])
    print("-------------")
    print(board[4],"|", board[5],"|", board[6],"|", board[7])
    print("-------------")
    print(board[8],"|", board[9],"|", board[10],"|", board[11])
    print("-------------")
    print(board[12],"|", board[13],"|", board[14],"|", board[15])
    print("")

def gameOver():
    global board
    global board2
    if board == board2:
        return True
    else:
        return False
    board = board2

def GameOver() :
    global Grille,GrilleMémoire,m
    GrilleMémoire=Grille
    p=1
    for n in range(0,3):
        m=Entrée[n]
        Décalage()
        for a in range(0,16):
            p=p*Grille[a]
    if p==0:
        return False
    else:
        return True

gen()
gen()
affichage()
while gameOver() == False :
    if IA == True:
        m=Entrée[random.randint(0,3)]
    else:
        m = input("mouvement ? (h, d, g, b): ")
    move()
    if board != board3:
        gen()
    board3 = board[:]
    affichage()
