import math
import random
from tkinter.messagebox import *
from tkinter import *

Mots=int(input("Nombre de Mots: "))
MotsInitiaux=Mots
Liste=[0]*Mots
ListeSortie=[]
for a in range(0,Mots):
    Liste[a]=a+1
for a in range(0,Mots):
    Random=random.randint(0,Mots-a-1)
    ListeSortie.append(Liste[Random])
    del Liste[Random]
Liste=ListeSortie

Mots=len(Liste)-1

def main():
    global Liste
    print(Liste)
    if len(Liste)>0:
        Mots=len(Liste)-1
        print("Mot: [",Liste[0],"]","                   Mots restants:",len(Liste),)
        aff()
    else:
        fenetre.quit()

def Oui():
    global Liste
    del Liste[0]
    main()

def Moyen():
    global Liste
    Random=random.randint(Mots//4,Mots//2)
    ListeSortie=Liste[:Random]
    ListeSortie.append(Liste[0])
    for a in range(Random,len(Liste)):
        ListeSortie.append(Liste[a])
    Liste=ListeSortie
    del Liste[0]
    main()
        
def Non():
    global Liste
    Random=random.randint(3*Mots//4,Mots)
    ListeSortie=Liste[:Random]
    ListeSortie.append(Liste[0])
    for a in range(Random,len(Liste)):
        ListeSortie.append(Liste[a])
    Liste=ListeSortie
    del Liste[0]
    main()

def aff():
    global txt
    canvas.delete(txt)
    txt = canvas.create_text(100, 50, text=Liste[0], font="Arial 50 italic", fill="white")
    canvas.pack()
    
fenetre=Tk()

label = Label(fenetre, text="Connaissez-vous ce mot?", bg="grey")
label.pack()
Button(text='Oui', command=Oui).pack()
Button(text='Moyen', command=Moyen).pack()
Button(text='Non', command=Non).pack()
Button(text='Quitter', command=fenetre.quit).pack()

canvas = Canvas(fenetre, width=200, height=100, background='black')
txt = canvas.create_text(100, 50, text=Liste[0], font="Arial 50 italic", fill="white")
canvas.pack()

fenetre.mainloop()
fenetre.destroy()

fenetre2=Tk()
label = Label(fenetre2, text="Vous connaissez vos mots, vous êtes trop chauds!", bg="grey")
label.pack()
fenetre2.mainloop()
fenetre2.destroy()

