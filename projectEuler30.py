import math
import time

def sumDigits(nb):
    s = 0
    nb = str(nb)
    for digit in nb:
        s += pow(int(digit), 5)
    return s

s = 0
for n in range(2, 354294):
    if n == sumDigits(n):
        s += n
print(s)
