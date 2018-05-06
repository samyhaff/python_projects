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
f=Width
g=Height

for y in range(0,g,6):
    for x in range(0,f,4):
        r=random.randint(0,1)
        if r==0:
            txt = canvas.create_text(x,y, text="0", font="Arial 6 italic", fill="green")
        if r==1:
           txt = canvas.create_text(x,y, text="1", font="Arial 6 italic",  fill="green")
                

mainloop()
