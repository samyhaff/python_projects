import time
from projectEuler60 import parties1, parties2, isPrime_, isPrime

t1 = time.time()
isPrime(1234567891)
t2 = time.time()
print(t2 - t1)

"""
parties1: 0.002737760543823242
parties2: 0.00011420249938964844
isPrime_: 0.003960847854614258
isPrime: 0.0018618106842041016
"""
