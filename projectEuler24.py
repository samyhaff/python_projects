import time
import math

def permutations(chaine):
    global c
    if len(chaine) == 1:
        return [chaine]

    perms = permutations(chaine[1:])
    char = chaine[0]
    result = []

    for perm in perms:
        for i in range(len(perm) + 1):
            result.append(perm[:i] + char + perm[i:])
            c = len(result)
    return (result)

result = permutations("0123456789")
print(c)
