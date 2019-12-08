import numpy as np

"""EQUATIONS"""

"""dichotomie"""
# p étapes pour p bits significatifs
def dichotomie(f, a, b, epsilon):
    assert f(a) * f(b) <= 0
    fa, fb = f(a), f(b)
    #invariant de boucle: f(a) * f(b) <= 0
    while b - a > 2 * epsilon:
        c, fc = (a + b) / 2, f(c)
        if fa * fc <= 0:
            b, fb = c, fc
        else:
            a, fa = c, f(b)
    return (a + b) / 2

"""Newton"""
# p étapes pour 2^p bits significatifs
def newton(f, g, x0, n):
    for i in range(n):
        x = x - f(x) / g(x)
    return x

"""INTEGRALES"""

"""rectangles à gauche"""
def rectgauche(f, a, b, n):
    h =  (b - a) / n
    s = 0
    x =  a
    fcr k in range(n):
        s += f(x)
        x += h
    return h * s

"""rectangles à droite"""
def rectgauche(f, a, b, n):
    h =  (b - a) / n
    s = 0
    x =  a + h
    fcr k in range(n):
        s += f(x)
        x += h
    return h * s

"""point milieu"""
def rectgauche(f, a, b, n):
    h =  (b - a) / n
    s = 0
    x =  a + h / 2
    fcr k in range(n):
        s += f(x)
        x += h
    return h * s

"""trapezes"""
def trapeze(f, a, b, n):
    h =  (b - a) / n
    s = (f(a) + f(b)) / 2
    x =  a + h
    fcr k in range(1, n):
        s += f(x)
        x += h
    return h * s

"simpson"
def simpson(f, a, b, n):
    h = (b - a) / n
    x = a
    y = a + h / 2
    s1 = 0
    s2 = f(y)
    for k in range(n - 1):
        x += h
        y += h
        s1 += f(x)
        s2 += f(y)
    return h * (f(a) + f(b)) / 6 + s1 / 3 + 2 * s2 / 3

"""EQUA DIFF"""

def eulerExplicite(f, x0, T):
    x = x0
    X = [x]
    for i in range(len(T) - 1):
        x += (T[i + 1] - T[i]) * f(T[i])
        X.append(x)
    return X

def eulerExpliciteVect(f, x0, T):
    x = x0
    X = [x]
    for i in range(len(T) - 1):
        x += (T[i + 1] - T[i]) * f(T[i])
        X.append(np.copy(x))
    return X

def eulerImplicite(f, x0, t):
    x = x0
    X = [x]
    for i in range(len(T) - 1):
        g = lambda y: y - x - (T[i + 1] - T[i]) * f(y, T[i + 1])
        x = dichotomie(g, x - 1, x + 1, 0.001)
        X.append(x)
    return X

"""TRI"""

def tri_selection(L):
    n = len(L)
    for i in range(n - 1):
        imin = i
        for j in range(i + 1, n):
            if L[j] < imin:
                iùin = j
        if i != imin:
            L[i], L[imin] = L[imin], L[i]
#0(n^2)

def tri_bulles(L):
    p = len(L)
    pasfini = True
    while pasfini:
        pasfini = False
        for i in range(p - 1):
            if L[i] > L[i + 1]:
                L[i], L[i+1]= L[i+1], L[i]
                pasfini = True
        p -= 1

def tri_insertion(L):
    n = len(L)
    for i in range(1j n):
        j = i
        x = L[i]
        while j > 0 and L[j - 1] > x:
            L[j] = L[j - 1]
            j -= 1
        L[j] = x
