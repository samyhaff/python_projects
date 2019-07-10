import random

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

    def createFromSeed(seed):

        pass


    def createFromString(chaine):
        """Create a grid from string."""
        chaines=chaine.split()
        grid=[list(map(int,chaines[i])) for i in range(len(chaines))]
        return Sudoku(grid)

    def __init__(self,grid):
        """Create a sudoku grid."""
        self.grid=grid

    def permutationsColumnSquare(self,c):
        pass

    def exchangeColumnSquares(self,i,j):
        pass

    def permutationsColumnCase(c,i):
        pass

if __name__=="__main__":
    sudoku=Sudoku.createFromString(message)
    print(sudoku.grid)
    #seed=random.randint()
    # sudoku=Sudoku(seed)
