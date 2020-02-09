import galois
import numpy as np

# t =

def gen():
    g = [1]
    for i in range(1, 2 * t + 1):
        g = g * Polynome([1, power(2, i)])
    return g

def encodage(A):
    _, B = A * Polynome(([0] * (2 * t)) + [1]) / gen(t)
    C =  A * Polynome(([0] * (2 * t)) + [1]) + B
    return C

# D est le message reçu
def verif(D):
    for i in range(1, 2 * t + 1):
        if D.eval(2 ** i) != 0:
            # il y a eu une erreur lors de la réception
            return False
    # D = C, il n y a pas d'erreurs
    return True

"""Supposons D != C, D = C + E et que le nombre d'erreurs est inférieur à t"""

def syndromes(D):
    return [D.eval(2 ** i) for j in range(1, 2 * t + 1)]

def systeme(D):
    S = syndromes(D)
    n = t # n correspond au nb d'erreurs
    det = 0
    while det != 0:
        M = np.empty(n)
        B = np.array([S[t + j + 1] for j in range(0, len(S))])
        for j in range(0, n):
            for i in range(0, n):
                a[j][i] = S[t + j - i]
        n = n - 1
        det = np.linalg.det(M)
    return (n, M, B)

def correction(D):
    S = syndromes(D)
    sys = systeme(D)
    n = sys[0]
    coeffs = np.linalg.solve(sys[1], sys[2])
    lambda = Polynome(coeffs)
    racines = []
    for i in range(0, 256):
        if lambda(2 ** i) == 0:
            racines.append(2 ** i)
    xr = [inverse(r) for r in racines]
    rangs = []
    # rangs des erreurs
    for i in range(0, 256):
        if xr.count(2 ** i) > 0:
            rangs.append(i)
    # valeur des erreurs
    M = np.empty(n)
    B = np.array(S for j in range(0, n))
    for j in range(0, n):
        for r in range(0, n):
            M[j, i] = xr[r + 1] ** (j + 1)
    erreurs = np.linalg.solve(M, B)
    E = polynome(erreurs)
    C = D + E
    return C
