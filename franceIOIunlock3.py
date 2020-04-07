n = nbLettres = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"

lignes = [[alphabet[0]] * (2 * n - 1)]
for i in range(1, n):
    ligne = lignes[i - 1][:]
    for j in range(i, 2 * n - 1 - i):
        ligne[j]= alphabet[i]
    lignes.append(ligne)
for i in range(0, n):
    print("".join(lignes[i]))
for i in range(n - 2, -1, -1):
    print("".join(lignes[i]))



nbLivres,nbJours = map(int,input().split(" "))
bibli = [0]*nbLivres

for i in range(nbJours):
    nbClients = int(input())
    for i in range(nbClients):
        indice, duree = map(int, input().split(" "))
        if bibli[indice]==0: #livre libre
            bibli[indice] = duree
            print(1)
        else: #libre oqp
            print(0)
    bibli = [max(duree-1, 0) for duree in bibli] #Jour suivant



notes=list(input())

def testRedondance(longueurPhrase,phrase) :
    for i in range(1,longueurPhrase) :
        if phrase[i]==phrase[i-1] :
            return 0
    return 1

while testRedondance(len(notes),notes)==0 :
    for i in range(1,len(notes)) :
        if notes[i]==notes[i-1] :
            del notes[i]
            del notes[i-1]

phrase="".join(notes)
print(phrase)



# import sys
# n = 7
# diffMax = 1.120
n = int(input())
diffMax = float(input())
# l1 = [float(input()) for i in range(n)]
l1 = []
for i in range(n):
    l1.append(float(input()))
# l1 = [1.292, 1.343, 3.322, 4.789, -0.782, 7.313, 4.212]
# l1 = [*map(float, [e for e in sys.stdin])]
l2 = l1[:]

def diffTest(l, diffMax):
    for i in range(len(l)-1):
        if abs(l[i]-l[i+1]) > diffMax:
            return True
    return False

e = 0
while diffTest(l1, diffMax):
    for i in range(1,n-1):
        l2[i] = (l1[i-1] + l1[i+1])/2
    l1=l2[:]
    e+=1

print(e)
