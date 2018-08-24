import math
import time

items = []
for a in range(2, 101):
    for b in range(2, 101):
        if items.count(pow(a, b)) == 0:
            items.append(pow(a, b))
        if items.count(pow(b, a)) == 0:
            items.append(pow(b, a))

print(len(items))
