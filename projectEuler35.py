import time
import math

def retCircular(prime):
    prime_str = str(prime)
    family = [prime]
    for _ in range(len(prime_str)-1):
        prime_str = prime_str[1:] + prime_str[0]
        child = int(prime_str)
        if child == prime:
            break
        family.append(int(prime_str))
    return family

print(retCircular(123))

def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def isPrimeAll(n):
    for p in retCircular(n):
        if not isPrime(int(p)):
            return False
    return True

s = 0
for n in range(2, 1000001):
    if isPrimeAll(n):
        s += 1
print(s)
