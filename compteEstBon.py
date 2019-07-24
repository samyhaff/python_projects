"""
objectif = int(input("saisir le nb a obtenir: "))
n = int(input("saisir la quantité de nombres disponibles: "))
nb = []
for i in range(n):
    nb.append(int(input().strip()))
"""

objectif = 123
nb = [4,5,6,7,8,9]

def couples(A):
    ans = []
    n = len(A)
    for i in range(n - 1):
        for j in range(i, n):
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
    B = A[:]
    a, b = couple
    B.remove(a)
    B.remove(b)
    B.append(result)
    return B

def resoudre(nb):
    global objectif
    for couple in couples(nb):
        for result in operations(couple):
            if result == objectif:
                return True
            if resoudre(adapt(nb, result, couple)):
                return True
    return False

if __name__ == "__main__":
    if resoudre(nb):
        print("Le compte est bon!")
    else:
        print("Pas de solution :(")
