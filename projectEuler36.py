import math
import time

def is_palindromic(n):
    d = n.digits()
    if len(d) == 1: return True
    for i in range(floor(len(d)/2)):
        if d[i] != d[len(d)-1-i]: return False
    return True

def is_b_palindromic(n):
    n = ZZ(bin(n).split('0b')[1])
    return is_palindromic(n)

s = 0
for n in range(1000000):
    if is_palindromic(ZZ(n)) and is_b_palindromic(ZZ(n)): s += n
print(s)

'''
from pythonds.basic.stack import Stack

def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString
'''
