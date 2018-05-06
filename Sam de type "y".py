from math import sqrt
import sys

n = int(input("nb = ")) #nb a tester
sn = int(sqrt(n))
i = 3

if n%i == 0:
    print("nb non premier")
    sys.exit()

while i <= sn and n%i != 0:
        i = i+2
            
if n%i != 0:
    print("nb premier")
if n%i == 0:
    print("nb non premier")
