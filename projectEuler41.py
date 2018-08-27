def testNb(nb):
    digits = []
    c = 0
    n = 0
    for digit in str(nb):
        if digit > n:
            n = digit
        digits.append(int(digit))
    for i in range(1, int(n)):
        if digits.count(i) != 1:
            return 0
        c = c + 1
    return c

def isPrime(n):
    if n in {2, 3, 5, 7}:
        return True
    if n < 2 or n%2 == 0:
        return False
    if n%3 == 0 or n%5 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0 or n%(f+2) == 0:
            return False
        f += 6
    return True

max_prime_digits = 0
max_prime = 2
for i in range(1, 7654322, 2):
    if isPrime(i):
        if testNb(i) >= max_prime_digits:
            max_prime_digits = testNb(i)
            max_prime = i
print(max_prime)
