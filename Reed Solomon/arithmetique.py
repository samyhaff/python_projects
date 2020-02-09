import math

def phi(n):
    c = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            c += 1
    return c
