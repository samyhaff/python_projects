import math
import random
import time

i = 2
j=1
testx = 0
testy = 0
number = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
longueur = len(number) - 1

while i<longueur+2:
    j=i*j
    i+=1
facto=j
i=0
print(facto-1)
while i < facto:
    print(number)
    testx=0
    testy=0
    trouve=0
    trouve2=0
    for x in range(1, longueur):
        if number[longueur-x] < number[longueur-x+1] and trouve==0:
            testx = longueur-x
            trouve=1
    for y in range(0, longueur):
        if number[longueur-y] > number[testx] and trouve2==0:
            testy = longueur-y
            trouve2=1
    copy = number[:]
    number[testx] = copy[testy]
    number[testy] = copy[testx]
    copy = number[:]
    k=0
    j=0
    number=[]
    while k<=testx:
        number.append(copy[k])
        k+=1
    copy.reverse()
    while j<longueur-testx:
        number.append(copy[j])
        j+=1
    copy = number[:]
    i = i + 1
