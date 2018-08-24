import math

o = 0
m = 0
c = 1
for i in range(1, 1000000):
    o = c
    c = 1
    t = i
    while t != 1:
        if t % 2 == 0:
            t = t / 2
        else:
            t = 3 * t + 1
        c = c + 1
    if c > o:
        m = i

print(m)
