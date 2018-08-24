import math

a = 1000

for i in range(1, a):
    for j in range(1, a):
        c = pow(i, 2) + pow(j, 2)
        if math.sqrt(c) == math.floor(math.sqrt(c)):
            if i + j + math.sqrt(c) == 1000:
                print(j * i * math.sqrt(c))
