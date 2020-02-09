import math

def pgcd(a, b):
    if abs(a) < abs(b):
        return pgcd(b, a)
    if abs(b) == 0:
        return (a, b)
    r = a % b
    return pgcd(b, r)

def phi(n):
    c = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            c += 1
    return c

def listePhi(n):
    return [0] + [phi(i) for i in range(1, n + 1)]

def val(k, p):
    v = 0
    while p % k == 0:
      v += 1
      p = p / k
    return v

def multiple(l, p):
    n = len(l)
    for k in range(0, n):
        r = val(l[k], p)
        if r != 0:
            l[k] = l[k] * (p - 1) * (p ** (r -1))

def estPremier(n):
    if n in {2, 3, 5, 7}:
        return True
    if n < 2 or n%2 == 0:
        return False
    if n%3 == 0 or n%5 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0 or n%(f+2) == 0:
            return False
        f += 6
    return True

def -listeP(n):
    l = []
    for i in range(1, n + 1):
        if estPremier(i):
            l.append(i)
    return l

def mu(n):
    if n == 1:
        return 1
    l = listeP

def prime(n):
    if n in {2, 3, 5, 7}:
        return True
    if n < 2 or n%2 == 0:
        return False
    if n%3 == 0 or n%5 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0 or n%(f+2) == 0:
            return False
        f += 6§
    return True

def piprime(n):
