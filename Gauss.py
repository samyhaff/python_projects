import numpy as np

A = np.array([[1,2,3], [4,5,6], [7,8,9]], dtype = float) # que des matrices carrées !!!!!!!!
n = len(A[0])
print(n)
I = np.identity(n)

def pivot(A, b, j):
    """choisis un pivot dans la je colonne de module max"""
    m = A[j][j]
    x = j
    for i in range(j + 1, n):
        if abs(A[i][j]) > abs(m):
            m = A[i][j]
            x =
    if x != i:
        A[[x, j]] = A[[j, x]]
        b[[x, j]] = b[[j, x]]

def elimination_bas(A, b, j):
    """elimine les coeffs sous A[j][j]"""
    for i in range(j + 1, n):
        A[i] = A[i] - (A[i][j] / A[j][j]) * A[j]
        b[i] = b[i] - (b[i][j] / b[j][j]) * b[j]

def descente(A, b):
    """transforme A en matrice triangulaire inférieure"""
    for k in range(n - 1):
        p = pivot(A, b, k)
        elimination_bas(A, b, k)

def elimination_haut(A, b, j):
    """élimine les coeffs du haut"""
    for i in range(j):
        A[i] = A[i] - (A[i][j] / A[j][j]) * A[j]
        b[i] = b[i] - (b[i][j] / b[j][j]) * b[j]

def remontee(A, b):
    """transfome A en matrice diagonale"""
    for j in range(n - 1, 0, -1):
        elimination_haut(A, b, j)

def solve_diagonal(A, b):
    for k in range(n):
        b[k] = b[k] / A[k, k]
    return b

def gaus(A, b):
    X = A.copy()
    Y = A.copy()
    descente(X, Y)
    remontee(X, Y)
    return solve_diagonal(X, Y)

def inverse(A):
    return gauss(A, I)
