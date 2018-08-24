import math
import time

l = 28123 # upper limit

abondant = []
for i in range(12, l):
    s = 1
    for k in range(2, int(math.sqrt(i))+1):
        if i % k == 0:
            s += k
            if k != i//k:
                s += i//k
    if s > i:
        abondant.append(i)

'''
def check(nb):
    for a in abondant:
        for b in abondant:
            if a + b == nb:
                return False
    return True
'''

def get_combinations():
    return set(a+b for a in abondant for b in abondant)

def main():
    comb = get_combinations()
    non_abondant = filter(lambda nb: nb in comb, range(12,l))
    return sum(non_abondant)

start = time.time()
print(main())
end = time.time()
print("le programme a mis ", end - start, " ms")
