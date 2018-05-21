from Fonctions import*
from math import sqrt
import time

Premiers=SortirVariable("ListeDesPremiers")[0]

def Décomposer(a,d=2):
    global memory
    Tests=Premiers[Premiers.index(d):]
    for i in Tests:
        if a%i==0:
            return [i]+Décomposer((a//i),i)
    if a<=Premiers[-1] or a==memory:
        return [a]
    else:
        memory=a
        return Décomposer(a,2)

début=time.time()
memory=0
D=Décomposer(int(input("Nombre à Décomposer: ")))
if D[-1]==1:
    del D[-1]
print(time.time()-début)
print(D)

