import numpy as np
import matplotlib.pyplot as plt

def secante(x0, x1, f, epsilon, maxIter):
    xAvant = x0
    k=0
    while abs(x − xAvant) > epsilon and k < maxIter:
        k = k + 1
        tau = (f(x) − f(xAvant)) / (x − xAvant)
        xAvant = x
        x = x − f(x) / tau
    return x

def Newton(x0, f, fPrime, epsilon, maxIter):
    x = x0
    xAvant = x0 + 10 ** 10
    k=0
    while abs(x − xAvant) > epsilon and k < maxIter:
        k = k + 1
        xAvant = x
        x = x − f(x) / fPrime(x)
    return x

def EulerExplicite(y0, f, t0, t1, N):
    h = (t1−t0) / N
    y = y0
    solution = np.zeros(N + 1)
    solution[0] = y0
    t = t0
    for i in range(1, N+1):
        y = y + h * f(y, t)
        solution[i] = y
        t += h
    return solution

# équation différentielle du premier ordre: y′ = t sin(y)
def f(y,t):
    return t∗np.sin(y)

def EulerExplicite2eOrdre(Y0, F, N, T):
    y = np.zeros(N)
    v = np.zeros(N) # v contient y’
    h = T / N
    y[0] = Y0[0]
    v[0] = Y0[1]
    for k in range(N−1):
        v[k] = v[k] + h * F(y, v, t)[0]
        y[k] = y[k] + h * F(x, y, t)[1]
    return y, v


def base10(x, b=2):
    s = 0
    k = len(x) − 1
    for a in x:
        s += int(a) * b ** k
        k −= 1
    return s

def baseb(x, b=2):
    s = ''
    y = x
    while y > 0:
        s = str(y % b) + s
        y //= b
    return s

def dicho(f, a, b, epsilon=1e−12):
    if f(a) * f(b) > 0:
        return None
    u, v = a, b
    while abs(v − u) > 2 * epsilon:
        w = (u + v) / 2
        if f(u) * f(w) <= 0:
            v = w
        else:
            u = w
    return (u + v) / 2
