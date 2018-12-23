lim = [1, 2, 4, 10, 20, 40, 100, 200]
compteur = [0, 0, 0, 0, 0, 0, 0, 0]
coeffs = [200, 100, 50, 20, 10, 5, 2, 1]
lim.reverse()
compteur.reverse()
coeffs.reverse()

def updateCompteur():
    compteur[0] += 1
    for i in range(0, len(compteur) - 1):
        if compteur[i] == lim[i]:
            compteur[i] = 0
            compteur[i + 1] += 1

def Sum():
    s = 0
    for i in range(0, len(compteur)):
        s += compteur[i] * coeffs[i]
        if s == 200:
            return True
    return False

c = 8
while compteur[7] != lim[7] + 1:
    updateCompteur()
    if Sum():
        c += 1
print(c)
