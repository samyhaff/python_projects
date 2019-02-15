import time
from time import time

def coupe_min3(a):
    c = m = a[0]
    for i in range(1, len(a)):
        c = min(c + a[i], a[i])
        m = min(m, c)
    return m

debut = time()

coupe_min3([1,2,3])
fin = time()

print(fin - debut)
