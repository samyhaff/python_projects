"""BUT: placer 8 reines de façon à ce qu'aucune d'elles ne soit attaquée"""

import numpy as np

board = np.zeros(shape = (8, 8))

def listAttack(coord, plateau):
    """retourne une liste avec la valeur des cases attaquées"""
    i, j = coord
    attacked = []
    for piece in plateau[i]:
        attacked.append(piece)
    for piece in plateau[:][j]:
        attacked.append(piece)
    k = 1
    while i + k < 8 and j + k < 8:
        attacked.append(plateau[i + k][j + k])
        k += 1
    k = 1
    while i - k >= 0 and j - k >= 0:
        attacked.append(plateau[i - k][j - k])
        k += 1
    return attacked

def condition(plateau):
    """retourne vrai si toutes les reines sont en sécurité, false sinon"""
    queens = []
    for i in range(8):
        for j in range(7):
            if plateau[i][j] == 1:
                queens.append((i, j))
    if len(queens) < 8:
        return False
    for queen in queens:
        if listAttack(queen, board).count(1) > 2:
            return False
    return True

def getMove(plateau):
    moves = []
    for i in range(8):
        for j in range(8):
            if plateau[i][j] == 0:
                moves.append((i, j))
    return moves

def backtrack(plateau):
