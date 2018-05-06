from math import sqrt
import time
from fractions import gcd

n = int(input("jusqu'a quel nombre tester? "))
a = 2
c = 0
d = 2

start_time = time.clock()

for p in range(2, n):
        while gcd(a, p) != 1:
                a = a + 1
        if a**(p-1) % p == 1:
                d = a +1
                while gcd(d, p) != 1:
                        d = d+1
                if d**(p-1) % p == 1:
                        print(p)
                        a = 2
                        d = 2
                        c = c + 1 

print(c, "nombres premiers")
#print("taux d'erreur: ", 0.5**n*100, "%")
print("fini en", time.clock() - start_time, "secondes")
