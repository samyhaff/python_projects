import math

def check(nb):
    if nb == 2:
        return True
    elif nb % 2 == 0:
        return False
    for k in range(3, int(math.floor(math.sqrt(nb))) + 1, 2):
        if nb % k == 0:
            return False
    return True

sum = 2
for i in range(3, 2000000, 2):
    if check(i):
        sum += i

print(sum)
