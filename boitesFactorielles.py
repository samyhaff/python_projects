import sys

nb = int(next(sys.stdin))

def maxFact(n):
    i = 1
    e = 1
    while e * (i + 1) <= n:
        i += 1
        e *= i
    return [i,e]

def decomp(n):
    m,f=maxFact(n)
    l = [0]*m
    for i in range(m,0,-1):
        l[i-1] = int(n//f)
        n = n%f
        f /= i
    return l

l = decomp(nb)
print(len(l))
print(" ".join(map(str,l)))
