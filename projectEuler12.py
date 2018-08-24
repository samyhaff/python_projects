import sys
sys.setrecursionlimit(100000)

'''

def gen(n):
    if n == 1:
        return 1
    else:
        return gen(n - 1) + n

'''

def check(i):
    c = 0
    for k in range(1, triangle + 1):
        if i % k == 0:
            c = c + 1
    if c >= 500:
        return True
    else:
        c = 0
        print(triangle)
        return False

'''

n = 1
while not check(gen(n)):
    n = n + 1
print(gen(n))

'''

triangle = 1
i = 2

while not check(triangle):
    triangle += i
    i += 1
print(triangle)
