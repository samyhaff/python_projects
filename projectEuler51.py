import math
n = 2

# peut être grandement ameliroé en stockant les nombres déjà trouvés dans un tableau
def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def toBin(x):
    s = ""
    y = x
    while y > 0: 
        s = str(y % 2) + s
        y = y // 2
    return int(s)

def parties(n, k):
    for i in range(2 ** n):
        index = toBin(i)

def find(n):
    pass

print(toBin(2))
