"""Import"""

import time
import random
import timeit
import pygame
import numpy

"""Variables"""

# board > case > square > pixel

# Dimensions of the board
board = (100,100)
board_line, board_column = board

# Dimensions of a case
case = (5,5)
case_line, case_column = case

# Dimensions of a case
square = (5,5)
square_line, square_column = square

board = [[0 for i in range(board_line)] for j in range(board_column)]

R = (255,  0,  0) # red
G = (  0,255,  0) # green
B = (  0,  0,255) # blue





DG = (  0,100,  0) # dark_green
greens=[G,DG]





grass = [[greens[random.randint(0,1)] for i in range(case_line)] for j in range(case_column)]

"""Fonctions"""

def print_case(object):

    increase = (10,10)
    xi,yi = increase
    window_size = (square_line*case_line*xi,square_column*case_column*yi)

    pygame.init()
    display = pygame.display.set_mode(window_size)
    pygame.display.set_caption("fenetre")

    done = False
    while not done:
        for y in range(case_column):
            for x in range(case_line):
                pygame.draw.rect(display, object[y][x], (x*xi,y*yi, (x+square_line)*xi,(y+square_column)*yi), 0)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
    pygame.quit()

"""Actions"""

print_case(grass)
