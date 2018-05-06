from math import sqrt
import math
import sys

P = int(input("P = "))                            #Nombre à tester
Probabilité = 1


C = 1
while P >= 10**C:
    C=C+1

M = P**C


if P%2 == 0:
    m = P+1
else:
    m = P

for a in range(m,M,P):
    A = a - 1
    if A%5 != 0 and A**2%P == 1 and (P-1)%2 == 0:
            Probabilité = Probabilité + 1
            print((2**Probabilité-2)/(2**Probabilité)*100,"/",100)

if P%2==0 or P%3==0 or P%5==0 or P%7==0 or P%11==0:
    sys.exit()
