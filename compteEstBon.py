import copy

"""
objectif = int(input("saisir le nb a obtenir: "))
n = int(input("saisir la quantité de nombres disponibles: "))
nb = []
for i in range(n):
    nb.append(int(input().strip()))
"""

objectif = 123
numbers = [4,5,6,7,8,9]

def couples(A):
    ans = []
    n = len(A)
    for i in range(n - 1):
        for j in range(i + 1, n):
            ans.append([A[i], A[j]])
    return ans

def operations(A):
    a, b = A
    ans = []
    ans.append(a + b)
    if a > b:
        ans.append(a - b)
    elif a < b:
        ans.append(b - a)
    if a % b == 0:
        ans.append(a // b)
    elif b % a == 0:
        ans.append(b // a)
    ans.append(a * b)
    return list(set(ans))

def adapt(A, result, couple):
    B = copy.deepcopy(A[:])
    a, b = couple
    B.remove(a)
    B.remove(b)
    B.append(result)
    return B

"(5*2)+4*5-2"

def resoudre(nb, objectif):
    for couple in couples(nb):
        for result in operations(couple):
            if result == objectif:
                return True
            new = adapt(nb, result, couple)
            if resoudre(new, objectif):
                return True
    return False

if __name__ == "__main__":
    if resoudre(numbers, objectif):
        print("Le compte est bon!")
    else:
        print("Pas de solution.")
