import time
import math

def permutations(chaine):
    if len(chaine) == 1:
        return [chaine]

    perms = permutations(chaine[1:])
    char = chaine[0]
    result = []

    for perm in perms:
        for i in range(len(perm) + 1):
            result.append(perm[:i] + char + perm[i:])

    return result

result = permutations("0123456789")
result.sort()
print(result[999999])
