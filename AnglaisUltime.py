import math
import random
from tkinter import *

Mots=int(input("Nombre de Mots: "))
MotsInitiaux=Mots
Liste=[0]*Mots
ListeSortie=[]

fenetre= Tk()
value=0
bouton1 = Radiobutton(fenetre, text="Oui", variable=value, value=1)
bouton2 = Radiobutton(fenetre, text="Non", variable=value, value=2)
bouton3 = Radiobutton(fenetre, text="Peu être", variable=value, value=3)
bouton1.pack()
bouton2.pack()
bouton3.pack()
fenetre.mainloop()

print(value)

print("")

for a in range(0,Mots):
    Liste[a]=a+1
for a in range(0,Mots):
    Random=random.randint(0,Mots-a-1)
    ListeSortie.append(Liste[Random])
    del Liste[Random]

Liste=ListeSortie

while len(Liste)>0:
    Mots=len(Liste)-1
    print("Mot: [",Liste[0],"]","                   Mots restants:",len(Liste),)
    Réponse=int(input("Réponse: "))
    if Réponse==0:
        Random=random.randint(2*Mots//5,3*Mots//5)
        ListeSortie=Liste[:Random]
        ListeSortie.append(Liste[0])
        for a in range(Random,Mots):
            ListeSortie.append(Liste[a])
        Liste=ListeSortie
        del Liste[0]
    if Réponse==1:
        Random=random.randint(3*Mots//4,Mots)
        ListeSortie=Liste[:Random]
        ListeSortie.append(Liste[0])
        for a in range(Random,Mots):
            ListeSortie.append(Liste[a])
        Liste=ListeSortie
        del Liste[0]
    if Réponse==2:
        del Liste[0]
    print("")

print("Vous connaissez vos mots, vous êtes trop chauds!")
