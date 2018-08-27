def isPrime(n):
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

def gen(nb):
    yield nb
    nb_str = str(nb)
    for k in range(1, len(nb_str)):
        yield int(nb_str[k:])
        yield int(nb_str[:-k])

def check(nb):
    for t in gen(nb):
        if not isPrime(t):
            return False
    return True

c = s = 0
i = 11
while c < 11:
    if check(i): # if all(map(isPrime, gen(i))):
        c += 1
        s += i
        print(i)
    i += 2

print('sum', s)
