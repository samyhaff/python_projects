from math import sqrt
import sys

n = int(input("Nombre = ")) #Nombre à tester
r = int(sqrt(n))
i = 3

while n%2 == 0:
    print(2," ",end="")
    n = n/2
while n%3 == 0:
    print(3," ",end="")
    n = n/3
while n != 1:
    while i <= n and n%i != 0:
        i = i+2
    print(i," ",end="")
    n = n/i

