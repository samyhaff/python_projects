import time
import math

max_c = 0
for p in range(2, 1001, 2):
    c = 0
    for a in range(2, p // 3 + 1):
        if (p*(p-2*a) % (2*(p-a)) == 0):
            c += 1
        if c > max_c:
            max_c = c
            max_p = p
print(max_p)
