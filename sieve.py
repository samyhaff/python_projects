""" Prime list generation """

def listPrimes(n):
    result = []
    prime = [True for i in range(n + 1)]
    p = 2

    while (p * p <= n):
		if prime[p]:
			for i in range(p * 2, n + 1, p):
				prime[i] = False
		p += 1

    for p in range(2, n):
		if prime[p]:
			result.append(p)

    return result

n = 101
primes = listPrimes(n)
