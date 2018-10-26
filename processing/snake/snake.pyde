import random
import math 

taille = 400
pas = 20
p = taille // (2 * pas)
snake = [[p - 2, p], [p - 1, p], [p, p], [p + 1, p], [p + 2, p]]
dir = 0

def setup():
    size(taille, taille) 
    background(0)
    stroke(255)
    fill(255)
    frameRate(2) 

def getDir():
    global dir
    if key == CODED:
        if keyCode == UP and dir != 3:
            dir = 1
        if keyCode == DOWN and dir != 1:
            dir = 3
        if keyCode == LEFT and dir != 0:
            dir = 2
        if keyCode == RIGHT and dir != 2:
            dir = 0

def drawSnake():
    global snake
    for coord in snake:
        ix = coord[0] 
        iy = coord[1]
        rect(ix * pas, iy * pas, pas, pas)
    
def move():
    global dir
    global snake
    if dir == 0:
        for i in range(0, len(snake)):
            snake[i] = (snake[i][0] + 1, snake[i][1])
    if dir == 2:
        for i in range(0, len(snake)):
            snake[i] = (snake[i][0] - 1, snake[i][1]
    
def draw():
    background(0)
    for i in range(pas, taille, pas):
        line(i, 0, i, taille) 
        line(0, i, taille, i)
    getDir()
    move()
    drawSnake()

    
