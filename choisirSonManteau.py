import sys

n = int(next(sys.stdin))
manteaux = []
for _ in range(n):
    manteaux.append(list(map(int, sys.stdin.readline().split(" "))))

def ordre(a, b):
    if a[0] < b[0]:
        return True
    elif a[0] > b[0]:
        return False
    return a[1] >= b[1]
