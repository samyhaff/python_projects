import math
import random
import time
i = 0
testx = 0
testy = 0
number = [1, 2, 3, 4, 5, 6, 7]
longueur = len(number) - 1
print(number)

while i < 5041:
    for x in range(0, 6):
        if number[x] < number[x + 1] and x > testx:
            testx = x
    for y in range(0, 7):
        if number[testx] < number[y] and y > testy:
            testy = y
    copy = number[:]
    number[testx] = copy[testy]
    number[testy] = copy[testx]
    number[testx + 1 : longueur].reverse()
    copy = number[:]
    print(number)
    i = i + 1
    textx = 0
    testy = 0
