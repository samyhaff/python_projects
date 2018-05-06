from tkinter import *
import math
import random

Width = 1440        #Ce sont les dimensions de mon écran sur mac
Height = 800        #tu devrais prendre les mêmes.
Eparsité=1          #Distance entre les points dans les lignes
Densité=5000       #Plus ou moins de lignes
TailleMoyenne=100   #C'est la taille moyenne des lignes dessinées aléatoirement

window = Tk()
canvas = Canvas(window, width = Width, height = Height, bg = "#000000")
canvas.pack()
img = PhotoImage(width = Width, height = Height)
canvas.create_image(Width // 2, Height // 2, image = img, state = "normal")


x=0
y=0
r=0                 #r c'est la rotation [[0,3]]
i=Width//2
j=Height//2
s=Eparsité
d=Densité
t=TailleMoyenne

for h in range(0,d):
    r=random.randint(0,3)
    for n in range(0,random.randint(0,t)):
        if r==0:
            x=x+1
        if r==1:
            y=y+1
        if r==2:
            x=x-1
        if r==3:
            y=y-1
        if x>i:
            x=-i
        if y>j:
            y=-j
        if x<-i:
            x=i
        if y<-j:
            y=j
        img.put("#ffffff", (s*x+i, s*y+j))
            

mainloop()
