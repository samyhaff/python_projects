from math import sqrt
import sys

p = int(input("p = "))                            #Nombre à tester
Probabilité = 1
Possibilité = 10

li(3,7,9,11,13,19,21,23,27,29,31,33,37,39,41,43,47,49,51

for a in range(2,Possibilité):
   if a%5 != 0 and a**(p-1) % p == 1:
        Probabilité = Probabilité + 1
        print((2**Probabilité-2)/(2**a)*100,"/",100)


