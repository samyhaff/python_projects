import time

def factorial(nb):
    if nb == 0:
        return 1
    return nb * factorial(nb - 1)

def Sum(nb):
    s = 0
    for digit in str(nb):
        s += factorial(int(digit))
    if s == nb:
        return True
    return False

s = 0
for n in range(3, 2540161):
    if Sum(n):
        s += n
print(s)
