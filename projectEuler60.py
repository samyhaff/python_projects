import math

listePremiers = []

def isPrime(n):
    global listePremiers
    if listePremiers.count(n) > 0:
        return True
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    listePremiers.append(n)
    return True

def parties2(A):
    # pas du tout efficace
    if A == []:
        return [[]]
    a = A[0]
    partiesPartielle = parties2(A[1:])
    reste = []
    for e in partiesPartielle:
        reste.append([a] + e)
    return reste + partiesPartielle

def cond(a, b, c, d, e):
    couples = []
    parties = parties2([a, b, c, d, e])
    if not isPrime(a) or not isPrime(b) or not isPrime(c) or not isPrime(d) or not isPrime(e):
        return False
    for partie in parties:
        if len(partie) == 2:
            p = [str(i) for i in partie]
            nb1 = int("".join(p + p[::-1]))
            nb2 = int("".join(p[::-1] + p))
            if not isPrime(nb1) or not isPrime(nb2):
                return False
    return True

a = 2
b = 2
c = 2
d = 2
e = 2
n = 2

while not cond(a, b, c, d, e):
    e = (e + 1) % n
    if e % n == 0: # saute la 1iere ittération mais on s'en fout
        d = (d + 1) % n
    if d % n == 0:
        c = (c + 1) % n
    if c % n == 0:
        b = (b + 1) % n
    if b % n == 0:
        a = (a + 1) % n
    if a % n == 0 and b % n == 0 and c % n == 0 and d % n == 0 and e % n == 0:
        n+=1

print(a+b+c+d+e)
