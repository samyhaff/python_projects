#2048 Graphique
#Wep c'est ça le talent!

#Marc est génial

from tkinter import *
import math
import random
import time

#Initialisation

gameOver=False
IA=False

Width = 500
Height = 500
cx=6
cy=6

l=Width//4//2
L=Height//4//2

Grille= [0, 0, 0, 0,
         0, 0, 0, 0,
         0, 0, 0, 0,
         0, 0, 0, 0]
Entrée=["g","h","d","b"]
Couleurs=["lemonchiffon","ivory2","ivory3","sandybrown","darkorange","brown2","firebrick1","gold","springgreen","steelblue","slateblue1","navy"]
m="0"
p=0

Difficulté=100

#Fin Initialisation

def Génération():
    Indice=[]
    Random=1
    for a in range(0,16):
        if Grille[a]==0:
            Indice.append(a)
    if len(Indice)>0 and random.randint(0,Difficulté)!=0:
        Random=random.randint(0,len(Indice)-1)
        Grille[Indice[Random]]=2*random.randint(1,2)

def Affichage(board):
    for y in range(0,4):
        for x in range(0,4):
            i=x+4*y
            j=0
            a=board[i]
            while a>=2:
                j=j+1
                a=a/2
            rectangle = canvas.create_rectangle((x+1/2)*Width//4-l+cx,(y+1/2)*Height//4-L+cy, (x+1/2)*Width//4+l+cx, (y+1/2)*Height//4+L+cy, fill=Couleurs[j%len(Couleurs)])
            if board[i]==0:
               txt = canvas.create_text((x+1/2)*Width//4+cx,(y+1/2)*Height//4+cy, text=board[i], font="Arial 40 italic", fill=Couleurs[0])
            if board[i]==2 or board[i]==4:
                txt = canvas.create_text((x+1/2)*Width//4+cx,(y+1/2)*Height//4+cy, text=board[i], font="Arial 40 italic", fill="black")
            if board[i]>4:
                txt = canvas.create_text((x+1/2)*Width//4+cx,(y+1/2)*Height//4+cy, text=board[i], font="Arial 40 italic", fill="white")
            canvas.pack()

def Décalage():
    for x in range(0,4):
        Décal1=[]
        for y in range(0,4):
            if m=="h" or m=="b":
                i=x+4*y
            if m=="g" or m=="d":
                i=4*x+y
            Décal1.append(Grille[i])
        if m=="b" or m=="d":
            Décal1.reverse()
        Décal2=[]
        for a in range(0,4):
            if Décal1[a]!=0:
                Décal2.append(Décal1[a])
        a=len(Décal2)
        for i in range(0,a-1):
            if Décal2[i]==Décal2[i+1]:
                Décal2[i]=2*Décal2[i]
                Décal2[i+1]=0
        for j in range(0,a-1):
            if Décal2[j]==0:
                del Décal2[j]
        Décal3=Décal2+(4-len(Décal2))*[0]
        if m=="b" or m=="d":
            Décal3.reverse()
        for y in range(0,4):
            if m=="h" or m=="b":
                i=x+4*y
            if m=="g" or m=="d":
                i=4*x+y
            Grille[i]=Décal3[y]

def GameOver() :
    global Grille,m
    p=0
    Grille2=Grille[:]
    for n in range(0,4):
        m=Entrée[n]
        Décalage()
        if Grille.count(0)==0:
            p=p+1
    if p==4:
        Affichage(Grille)
        time.sleep(5)
        window.quit()
    Grille=Grille2[:]

def GameOver1():
    if Grille.count(0)==0:
        window.quit()


def clavier(event):
    global m,Entrée
    touche=event.keysym
    if IA:
        while IA :
            m=Entrée[random.randint(0,3)]
            Génération()
            GameOver()
    else:
        if touche=="Up":
            m="h"
        if touche=="Down":
            m="b"
        if touche=="Right":
            m="d"
        if touche=="Left":
            m="g"
        if touche=="Escape":
            window.quit()
        Décalage()
        Génération()
        Affichage(Grille)
        GameOver()
        
window = Tk()
canvas = Canvas(window, width=Width+cx, height=Height+cy, bg="#ffffff")
canvas.pack()
img = PhotoImage(width=Width+cx, height=Height+cy)
canvas.create_image((Width//2+cx, Height//2+cy), image=img, state="normal")

for x in range(0,4):
    for y in range(0,4):
        rectangle = canvas.create_rectangle((x+1/2)*Width//4-l+cx,(y+1/2)*Height//4-L+cy, (x+1/2)*Width//4+l+cx, (y+1/2)*Height//4+L+cy, fill="white")
        canvas.pack()

Génération()
Génération()
Affichage(Grille)

canvas.focus_set()
canvas.bind("<Key>", clavier)

window.mainloop()
window.destroy()

print("La partie est finie")
