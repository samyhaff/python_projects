import math
import random
import numpy

#Initialisation

Sudoku = [[1,6,2,8,5,7,4,9,3],
          [5,3,4,1,2,9,6,7,8],
          [7,8,9,6,4,3,5,2,1],
          [4,7,5,3,1,2,9,8,6],
          [9,1,3,5,8,6,7,4,2],
          [6,2,8,7,9,4,1,3,5],
          [3,5,6,4,7,8,2,1,9],
          [2,4,1,9,3,5,8,6,7],
          [8,9,7,2,6,1,3,5,4]]

#Fonctions

def Générer(Grille):
    for Z in range(0,100):
        Liste=[0]*9
        C=random.randint(1,4)
        N=random.randint(0,2)
        O=(N+random.randint(1,2))%3
        for A in range(0,3):
            W=0
            for B in range(0,9):
                if C==1:
                    M=27*A+B+9*N
                    H=27*A+B+9*O
                if C==2:
                    M=3*A+9*B+N
                    H=3*A+9*B+O
                if C==3:
                    M=27*N+9*A+B
                    H=27*O+9*A+B
                if C==4:
                    M=3*N+A+9*B
                    H=3*O+A+9*B
                D=M%9
                E=M//9
                F=H%9
                G=H//9
                Liste[W]=Grille[D][E]
                Grille[D][E]=Grille[F][G]
                Grille[F][G]=Liste[W]
                W=W+1
    for D in range(0,9):
        for E in range(0,9):
            if random.randint(1,3)==1:
                Grille[D][E]=0

def AfficherNul(Grille):
    for E in range(0,9):
        print(Grille[E])

def Afficher(dboard):
    print(dboard[0], dboard[1], dboard[2], "|", dboard[3], dboard[4], dboard[5], "|", dboard[6], dboard[7],dboard[8])
    print(dboard[9], dboard[10], dboard[11], "|", dboard[12], dboard[13], dboard[14], "|", dboard[15], dboard[16],dboard[17])
    print(dboard[18], dboard[19], dboard[20], "|", dboard[21], dboard[22], dboard[23], "|", dboard[24], dboard[25], dboard[26])
    print("------+-------+------")
    print(dboard[27], dboard[28], dboard[29], "|", dboard[30], dboard[31], dboard[32], "|", dboard[33], dboard[34], dboard[35])
    print(dboard[36], dboard[37], dboard[38], "|", dboard[39], dboard[40], dboard[41], "|", dboard[42], dboard[43],dboard[44])
    print(dboard[45], dboard[46], dboard[47], "|", dboard[48], dboard[49], dboard[50], "|",  dboard[51],dboard[52], dboard[53])
    print("------+-------+------")
    print(dboard[54], dboard[55], dboard[56], "|", dboard[57], dboard[58], dboard[59], "|", dboard[60], dboard[61], dboard[62])
    print(dboard[63], dboard[64], dboard[65], "|", dboard[66], dboard[67], dboard[68], "|", dboard[69], dboard[70], dboard[71])
    print(dboard[72], dboard[73], dboard[74], "|", dboard[75], dboard[76], dboard[77], "|", dboard[78], dboard[79], dboard[80])


def TraduireEnListe(Grille):
    Liste=[0]*81
    for x in range(0,9):
        for y in range(0,9):
            Liste[x*9+y]=Grille[x][y]
    return Liste
    
def CompléterPS(Grille):
    return True

def Remplir(Liste)
    return Issues

def Résolveur(Grille):

    return Grille

Générer(Sudoku)
Afficher(TraduireEnListe(Sudoku))



