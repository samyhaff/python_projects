from tkinter import *
import math
import random

Width = 1440
Height = 800

Eparsité=3
Taille=250

s=Eparsité
t=Taille


window = Tk()
canvas = Canvas(window, width = Width, height = Height, bg = "#000000")
canvas.pack()
img = PhotoImage(width = Width, height = Height)
canvas.create_image(Width // 2, Height // 2, image = img, state = "normal")

#for x in range(Width):
#	for y in range(Height):
#		img.put("#ffffff", (x, y))


x=0
y=0

r=0

i=Width//2
j=Height//2

for h in range(0,t):
    r=(r+1)%4
    for n in range(0,h):
        if r==0:
            x=x+1
        if r==1:
            y=y+1
        if r==2:
            x=x-1
        if r==3:
            y=y-1
        img.put("#ffffff", (s*x+i, s*y+j))
            

mainloop()
