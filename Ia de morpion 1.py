import math
import numpy

M=[0]*9
Grille = [0]*9
Liste = np.zeros([9][8][7][6][5][4][3][2][1])
Enjeux = [[9,-5],
          [-9,8],
          [7,-4],
          [-8,6],
          [5,-3],
          [-7,4],
          [3,-2],
          [-6,2],
          [1,-1]]


for a in range(0,9):
    M[0]=a
    Avantage=Avantage+Enjeux[0,testwin(Grille)]/2**0
    for b in range(0,8):
        M[1]=b
        Avantage=Avantage+Enjeux[1,testwin(Grille)]/2**1
        for c in range(0,7):
            M[2]=c
            Avantage=Avantage+Enjeux[2,testwin(Grille)]/2**2
            for d in range(0,6):
                M[3]=d
                Avantage=Avantage+Enjeux[3,testwin(Grille)]/2**3
                for e in range(0,5):
                    M[4]=e
                    Avantage=Avantage+Enjeux[4,testwin(Grille)]/2**4
                    for f in range(0,4):
                        M[5]=f
                        Avantage=Avantage+Enjeux[5,testwin(Grille)]/2**5
                        for g in range(0,3):
                            M[6]=g
                            Avantage=Avantage+Enjeux[6,testwin(Grille)]/2**6
                            for h in range(0,2):
                                M[7]=h
                                Avantage=Avantage+Enjeux[7,testwin(Grille)]/2**7
                                i=1
                                M[8]=i
                                Avantage=Avantage+Enjeux[8,testwin(Grille)]/2**8
                                Liste[M]=Avantage
                                Mouvements=[0]*9
                                Avantage=0
                                
                                
                                
 
def testwin(grille):
    if (grille[0]==grille[1]) and (grille[0]==grille[2]) and (grille[0]!=0):
        return 1
    elif (grille[3]==grille[4]) and (grille[3]==grille[5]) and (grille[3]!=0):
        return 1
    elif (grille[6]==grille[7]) and (grille[6]==grille[8]) and (grille[6]!=0):
        return 1
    elif (grille[0]==grille[3]) and (grille[0]==grille[6]) and (grille[0]!=0):
        return 1
    elif (grille[1]==grille[4]) and (grille[1]==grille[7]) and (grille[1]!=0):
        return 1
    elif (grille[2]==grille[5]) and (grille[2]==grille[8]) and (grille[2]!=0):
        return 1
    elif (grille[0]==grille[4]) and (grille[0]==grille[8]) and (grille[0]!=0):
        return 1
    elif (grille[2]==grille[4]) and (grille[2]==grille[6]) and (grille[2]!=0):
        return 1
    else
        return 0
