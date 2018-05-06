import math
import random

found = 0
isComplete = 0
joueur = 3
n = 0 #best move

board = [0, 1, 2, #affichage
         3, 4, 5,
         6, 7, 8]
test = [0] * 9 #calculs

def affichage():
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])

def winAI(joueur):
    if (test[0]==test[1]) and (test[0]==test[2]) and (test[2]==test[1]) and (test[0]==joueur):
        return 1
    if (test[3]==test[4]) and (test[3]==test[5]) and (test[4]==test[5]) and (test[5]==joueur):
        return 1
    if (test[6]==test[7]) and (test[6]==test[8]) and (test[7]==test[8]) and (test[8]==joueur):
        return 1
    if (test[0]==test[3]) and (test[0]==test[6]) and (test[3]==test[6]) and (test[6]==joueur):
        return 1
    if (test[1]==test[4]) and (test[1]==test[7]) and (test[4]==test[7]) and (test[7]==joueur):
        return 1
    if (test[2]==test[5]) and (test[2]==test[8]) and (test[5]==test[8]) and (test[8]==joueur):
        return 1
    if (test[0]==test[4]) and (test[0]==test[8]) and (test[4]==test[8]) and (test[8]==joueur):
        return 1
    if (test[2]==test[4]) and (test[2]==test[6]) and (test[4]==test[6]) and (test[6]==joueur):
        return 1

def win(joueur):
    if (board[0]==board[1]) and (board[0]==board[2]) and (board[2]==board[1]) and (board[0]==joueur):
        return 1
    if (board[3]==board[4]) and (board[3]==board[5]) and (board[4]==board[5]) and (board[5]==joueur):
        return 1
    if (board[6]==board[7]) and (board[6]==board[8]) and (board[7]==board[8]) and (board[8]==joueur):
        return 1
    if (board[0]==board[3]) and (board[0]==board[6]) and (board[3]==board[6]) and (board[6]==joueur):
        return 1
    if (board[1]==board[4]) and (board[1]==board[7]) and (board[4]==board[7]) and (board[7]==joueur):
        return 1
    if (board[2]==board[5]) and (board[2]==board[8]) and (board[5]==board[8]) and (board[8]==joueur):
        return 1
    if (board[0]==board[4]) and (board[0]==board[8]) and (board[4]==board[8]) and (board[8]==joueur):
        return 1
    if (board[2]==board[4]) and (board[2]==board[6]) and (board[4]==board[6]) and (board[6]==joueur):
        return 1

def AI():
    global found
    global n
    for a in range(0, 9):
        if found != 1:
            if (board[a] != "x") and (board[a] != "o"):
                test[a] = 1 
                if winAI(1) == 1:
                    n = a
                    found = 1
                    break
                else:
                    test[a] = 2
                    if winAI(2) == 1:
                        n = a
                        found = 1
                        break
                    else:
                        for b in range(0, 9):
                            if found != 1:
                                if (board[b] != "x") and (board[b] != "o"):
                                    test[b] = 1 
                                    if winAI(1) == 1:
                                        n2 = a
                                        found = 1
                                        break
                                    else:
                                        test[b] = 2
                                        if winAI(2) == 1:
                                            n2 = b
                                            found = 1
                                            break                                
                                    test[b] = 0
                        board[n2] = "o"
                        test[n2] = 1                               
                test[a] = 0
    board[n] = "o"
    test[n] = 1
                                   
while (test.count(0) != 0) and (win("x") != 1) and (win("o") != 1):
    
    i = input("Choisir un spot:")
    i = int(i)

    if board[i] != "x" and board[i] != "o":
        board[i] = "x"
        test[i] = 2

        AI()
                
        found = 0        
    else:
        print("spot occupé")

    affichage()

if test.count(0) == 0:
    print("match nul") 
elif win("x") == 1:
    print("Vous avez gagné!")
else:
    print("Vous avez perdu")
                                                      


     
