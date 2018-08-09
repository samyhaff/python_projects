def factorielle(n):
    if n == 1:
        return 1
    return n * factorielle(n - 1)

print(factorielle(5))
