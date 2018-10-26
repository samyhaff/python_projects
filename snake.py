__author__="Marc Partensky"
__license__="Partensky Company"
__game__="Snake"

#------------#
#Dependencies#
#------------#

import pygame
import math
import random
import numpy as np

#---------#
#Variables#
#---------#

BLUE    = (  0,  0,255)
RED     = (255,  0,  0)
GREEN   = (  0,255,  0)
YELLOW  = (255,255,  0)
BLACK   = (  0,  0,  0)
WHITE   = (255,255,255)

RIGHT=0
TOP=1
LEFT=2
DOWN=3

#-------#
#Classes#
#-------#

class Map:
    def __init__(self):
        self.size=[20,20]
        self.board=np.zeros(self.size)
        self.color_case=BLACK
        self.color_background=WHITE

class Window:
    def __init__(self):
        self.title="Snake"
        pygame.init()
        info = pygame.display.Info()
        s=max(info.current_w//2,info.current_h//2)
        self.size=(s,s)
        self.screen=pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
        pygame.display.flip()

    def closed(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

    def select(self):
        done=False
        while self.closed():
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    return (event.pos[0],event.pos[1])

    def point(self):
        for event in pygame.event.get():
            return (event.pos[0],event.pos[1])

    def flip(self):
        pygame.display.flip()

    def showMap(self,map):
        self.screen.fill(map.color_background)
        mx,my=map.size
        sx,sy=self.size
        cx,cy=sx/mx,sy/my
        for x in range(mx):
            for y in range(my):
                pygame.draw.rect(self.screen, map.color_case, (cx*x+1,cy*y+1,cx-1,cy-1), 0)

    def showSnake(self,snake,map):
        mx,my=map.size
        sx,sy=self.size
        cx,cy=sx/mx,sy/my
        for coordonates in snake.body:
            x,y=coordonates
            pygame.draw.rect(self.screen, snake.color, (cx*x+1,cy*y+1,cx-1,cy-1), 0)

class Snake:
    def __init__(self):
        self.size=4
        self.body=[[8,10],[9,10],[10,10],[11,10]]
        self.direction=LEFT
        self.color=WHITE
        self.head=[8,10]

    def move():
        x,y=self.head
        if self.direction=LEFT:
            x,y=x-1,y
        if self.direction=RIGHT:
            x,y=x+1,y
        if self.direction=TOP:
            x,y=x,y-1
        if self.direction=DOWN:
            x,y=x,y+1
        self.head=x,y
        self.body=[self.head]+self.body[:-1]


class Food:
    def __init__(self):
        self.coordonates=np.random.randrange((2,2))
    def


class Game:
    def __init__(self):
        self.window=Window()
        self.map=Map()
        self.update=10
    def play(self):
        self.window.show(self.map)
        self.window.flip()
        while not self.window.closed():
            if
            self.window.show(self.map)
            self.window.flip()
