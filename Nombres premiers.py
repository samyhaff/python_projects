import math
from math import sqrt

Limite=int(input("Limite:"))

Liste=[2,3]
a=3

while len(Liste)<Limite:
    a=a+2
    b=sqrt(a)
    n=0
    while a/Liste[n]!=a//Liste[n] and Liste[n]<=b:
        n=n+1
    if Liste[n]>sqrt(a):
        Liste.append(a)

print(Liste)
a
