import random

class Puissance4:
    def __init__(self):
        self.board = Board()
        self.players = [Player(0),Player(1)]
        self.state = 0

    def __call__(self):
        while self.board.on:
            self.board.check()
            self.state += 1
            turn = self.state % 2
            player = self.players[turn]
            player(self.board)

class Board:
    def __init__(self,size=[7,6]):
        self.size = size
        self.grid = [[-1 for y in range(size[1])] for x in range(size[0])]
        self.on = True

    def check(self):
        sx,sy=self.size
        for x in range(sx):
            self.on=self.checkLine(self.grid[x])
        for y in range(sy):
            self.on=self.checkLine(self.grid[y])

    def checkLine(self,line):
        for x in range(len(line)):
            if line[]




    def randomfill(self):
        sx,sy=self.size
        for x in range(sx):
            for y in range(sy):
                self.grid[x][y]=random.randint(-1,1)

    def __repr__(self):
        text=""
        lx=[]
        for x in range(self.size[0]):
            ly=[]
            for y in range(self.size[1]):
                if self.grid[x][y]==-1:
                    ly.append(" ")
                if self.grid[x][y]==0:
                    ly.append("X")
                if self.grid[x][y]==1:
                    ly.append("O")
            lx.append("|".join(ly))
        text="\n".join(lx)
        return text

class Player:
    def __init__(self,side):
        self.side = side

    def __call__(self,board): #Jouer
        self.randomPlay(board)

    def randomPlay(self,board):
        a=list(range(self.size[0]))
        random.shuffle(a)
        for e in a:
            choice=self.choose(board,e)
            if choice is not None:
                x,y=choice
                board.grid[x][y]=self.side

    def choose(self,board,x):
        l=list(range(self.size[1]))
        l.reverse()
        for y in l:
            v=self.grid[x][y]
            if v==0 or v==1:
                return (x,y)
        return None


    def play(self,board,x):
        i = board.size[2]
        if board.grid[x].count(-1) == 0 or x > "grosse valeur inutile juset la pour que le programme plante pas quand je le test":
            while board.grid[x][i] != -1:
                i -= 1

game = Puissance4()
#game()

game.board.randomfill()
print(str(game.board))
