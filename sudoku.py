import random
import copy
#import numpy as np
#import pygame
#from pygame.locals import *

ultimate_grid = [[8,1,2,7,5,3,6,4,9],
                 [9,4,3,6,8,2,1,7,5],
                 [6,7,5,4,9,1,2,8,3],
                 [1,5,4,2,3,7,8,9,6],
                 [3,6,9,8,4,5,7,2,1],
                 [2,8,7,1,6,9,7,3,4],
                 [5,2,1,9,7,4,3,6,8],
                 [4,3,8,5,2,6,9,1,7],
                 [7,9,6,3,1,8,4,5,2]]

message="812753649 943682175 675491283 154237896 369845721 287169734 521974368 438526917 796318452"

class Sudoku:

    def createFromString(chaine):
        """Create a grid from string."""
        chaines=chaine.split()
        grid=[list(map(int,chaines[i])) for i in range(len(chaines))]
        return Sudoku(grid)

    def __init__(self,grid):
        """Create a sudoku grid."""
        self.grid=grid

    def initPygame(self):
        pass

    def exchangeLinesSquares(self,i,j):
        index1 = 3 * i
        for k in range(index1,index1+3):
            #self.grid[x1][y1],self.grid[x2][y2]=self.grid[x2][y2],self.grid[x1][y1]
            self.exchangeLinesCase(k, j*3+k)

    def exchangeLinesCase(self, i, j):
        self.grid[i],self.grid[j]=self.grid[j],self.grid[i]

    def exchangeColumnsSquares(self,j,i):
        index1 = 3 * i
        for k in range(index1,index1+3):
            #self.grid[x1][y1],self.grid[x2][y2]=self.grid[x2][y2],self.grid[x1][y1]
            self.exchangeLinesCase(k, j*3+k)

    def exchangeColumnsCase(self, i, j):
        c=copy.deepcopy(self.grid[:][j])
        print(s,end='\n'*2)
        self.grid[:][j]=copy.deepcopy(self.grid[:][i])
        print(s)
        self.grid[:][i]=c

    def show(self):
        """Show the sudoku on the screen."""
        pass

    def __str__(self):
        return "\n".join(map(str,[" ".join(map(str,c)) for c in self.grid]))

if __name__=="__main__":
    s=Sudoku.createFromString(message)
    #seed=random.randint()
    # sudoku=Sudoku(seed)
    print(s,end='\n'*2)
    s.exchangeColumnsCase(0,2)
    print(s)
