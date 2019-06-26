from math import log

def isNthPower(nb):
    a = log(nb, len(str(nb)))
    print(a)
    if a == int(a):
        return True
    return False

print(isNthPower(134217728))
