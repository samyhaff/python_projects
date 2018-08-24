import time
import math

nbList = []

def testNb(nb):
    digits = []
    for digit in str(nb):
        digits.append(int(digit))
    for digit in str(a):
        digits.append(int(digit))
    for digit in str(b):
        digits.append(int(digit))
    digits.sort()
    if digits == range(1, 10):
        nbList.append(nb)
        if nbList.count(nb) == 1:
            return True
    return False

# 1 * 4 ou 3 * 2

s = 0
for a in range(1, 10):
    for b in range(1000, 10000):
        n = a * b
        if testNb(n):
            s += n
for a in range(10, 100):
    for b in range(100, 1000):
        n = a * b
        if testNb(n):
            s += n
print(s)
