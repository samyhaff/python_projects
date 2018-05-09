import math
import copy
import numpy
import random



#Variable

Sudoku = [[1,6,2,8,5,7,4,9,3],
          [5,3,4,1,2,9,6,7,8],
          [7,8,9,6,4,3,5,2,1],
          [4,7,5,3,1,2,9,8,6],
          [9,1,3,5,8,6,7,4,2],
          [6,2,8,7,9,4,1,3,5],
          [3,5,6,4,7,8,2,1,9],
          [2,4,1,9,3,5,8,6,7],
          [8,9,7,2,6,1,3,5,4]]



#Fonctions:

def Vider(Grille):
    for D in range(0,9):
        for E in range(0,9):
            if random.randint(1,3)==1:
                Grille[D][E]=0
    return Grille

def Permuter(Grille):
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
    return Grille

def vLine(j,Test,Board):
    for i in range(9):
        if Board[j][i] == Test:
            return True
    return False

def vColumn(i,Test,Board):
    for j in range(9):
        if Board[j][i] == Test:
            return True
        return False

def vBlock(i,j,Test,Board):
    for I in range(3):
        for J in range(3):
            if Board[3*(j//3)+J][3*(i//3)+I] == Test:
                return True
    return False

def Validité(i,j,Test,Board):
    if vColumn(i,Test,Board)==False and vBlock(i,j,Test,Board)==False and vLine(j,Test,Board)==False:
        return True
    else:
        return False

def Compléter(Board,Initial,Liste):
    Indice=0
    X=0
    Y=0
    Board = copy.deepcopy(Initial)
    for i in range(len(Liste)):
        X=Indice%9
        Y=Indice//9
        while Board[Y][X]!=0:
            Indice+=1
            X=Indice%9
            Y=Indice//9
        Board[Y][X]=Liste[i]
        Indice+=1
    return Board

def Ajouter(Liste):
    Ajout=1
    for i in range(len(Liste)):
        Retenue=(Liste[len(Liste)-i-1]+Ajout)//9
        Liste[len(Liste)-i-1]=(Liste[len(Liste)-i-1]+Ajout)%9
        Ajout=Retenue
    return Liste

def Aff(matrice):
    for Y in range(9):
        print(matrice[Y])
    print("")


def CountMatrice(Board,Elément):
    Valeur=0
    for Y in range(len(Board)):
        Valeur=Valeur+Board[Y].count(Elément)
    return Valeur

def Main(Board):
    Liste=[1]
    Initial = copy.deepcopy(Board)
    while CountMatrice(Board,0)!=0:
        Indice=-1
        X=0
        Y=0
        Board = copy.deepcopy(Initial)
        for i in range(len(Liste)):
            Indice+=1
            X=Indice%9
            Y=Indice//9
            if Indice>=81:
                return Board
            while Board[Y][X]!=0:
                Indice+=1
                X=Indice%9
                Y=Indice//9
                if Indice>=81:
                    return Board
            Board[Y][X]=Liste[i]
        Board[Y][X]=0
        while Validité(X,Y,Liste[len(Liste)-1],Board)==False and Liste[len(Liste)-1]<=9:
            Liste[len(Liste)-1]=Liste[len(Liste)-1]+1
        Valide=Validité(X,Y,Liste[len(Liste)-1],Board)
        while Liste[len(Liste)-1]>9:
            if len(Liste)>1:
                del Liste[len(Liste)-1]
                Board[Y][X]=0
                Liste[len(Liste)-1]=Liste[len(Liste)-1]+1
            else:
                return Board
        if Validité(X,Y,Liste[len(Liste)-1],Board):
            Liste.append(1)
    return Board



#Actions:

Soluce=Permuter(Sudoku)
TheOne=Vider(Soluce)
Aff(TheOne)
Aff(Main(TheOne))

            
    
        
    
    
    
    
