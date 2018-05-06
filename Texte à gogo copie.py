import math
import random
import numpy as np
import os

#Texte à gogo copie

os.chdir("C:/tests python")
mon_fichier = open("/Users/olivierpartensky/Desktop/Programme/CryptoEntrée/Proust.txt", "r")
Message = mon_fichier.read()
mon_fichier.close()


Nombre_de_caractères_à_afficher=100  #Modifie ça stv
Taille=5                                #mais, ça pas touche pour l'instant

TMes=len(Message)
Caractères = []

for i in range(0,TMes):
    n=0
    Recherche=True
    while n<len(Caractères) and Recherche:
        if Caractères[n]==Message[i]:
            Recherche=False
        n=n+1
    if Recherche:
        Caractères.append(Message[i])

#print(Caractères)

Liste = np.zeros([len(Caractères)]*(Taille+1))

for i in range(Taille,TMes):
    Liste[Caractères.index(Message[i-5]),Caractères.index(Message[i-4]),Caractères.index(Message[i-3]),Caractères.index(Message[i-2]),Caractères.index(Message[i-1]),Caractères.index(Message[i])]+=1

#TSor=int(input("Taille: "))
TSor=Nombre_de_caractères_à_afficher

Sortie="Sans "
for i in range(Taille,TSor):
    if i<Taille:
        Sortie=Sortie+Caractères[random.randint(0,len(Caractères)-1)]
    else:
        SortiesPossibles=[]
        for n in range(0,len(Caractères)):
            a=int(Liste[Caractères.index(Sortie[i-5]),Caractères.index(Sortie[i-4]),Caractères.index(Sortie[i-3]),Caractères.index(Sortie[i-2]),Caractères.index(Sortie[i-1]),n])
            for m in range(0,a):
                SortiesPossibles.append(Caractères[n])
        if len(SortiesPossibles)==0:
            Sortie=Sortie+Caractères[random.randint(0,len(Caractères)-1)]
        else:
            Sortie=Sortie+SortiesPossibles[random.randint(0,len(SortiesPossibles)-1)]

#print(i)
#print(SortiesPossibles)
print(Sortie)
