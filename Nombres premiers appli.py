import math
from math import sqrt

Ajout=int(input("Ajouter:"))

ListeDesPremiers = open("ListeDesPremiers.txt", "r")
ChaineDesPremiers=ListeDesPremiers.read()
Chaine=ChaineDesPremiers.split(",")
Liste=[0]*len(Chaine)
for i in range(0,len(Chaine)):
    Liste[i]=int(Chaine[i])
ListeDesPremiers.close()

print(Liste)

ListeDesPremiers = open("ListeDesPremiers.txt", "a")
a=Liste[-1]

T=0
while T<Ajout:
    a=a+2
    b=sqrt(a)
    n=0
    while a/Liste[n]!=a//Liste[n] and Liste[n]<=b:
        n=n+1
    if Liste[n]>sqrt(a):
        T=T+1
        Liste.append(a)
        ListeDesPremiers.write(","+str(a))
ListeDesPremiers.close()
