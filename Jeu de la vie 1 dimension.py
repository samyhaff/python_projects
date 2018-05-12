from tkinter import *
import math
import random

Width = 1440
Height = 720

L1=[0]*Width
L2=[0]*Width
L3=[1,0,0,0,0,0,0,1]

w=Width
h=Height

L1[Width//2]=1

window = Tk()
canvas = Canvas(window, width=Width, height=Height, bg="#ffffff")
canvas.pack()
img = PhotoImage(width=Width, height=Height)
canvas.create_image((Width/2, Height/2), image=img, state="normal")

img.put("#000000", (Width//2,10))

for y in range(11,h):
    for x in range(1,w-1):
        for c in range(0,2):
            for b in range(0,2):
                for a in range (0,2):
                     if L1[x-1] == a and L1[x] == b and L1[x+1] == c :
                        L2[x] = L3[a+2*b+4*c]
        if L2[x]==1:
            img.put("#000000", (x,y))
    L1=L2[:]

mainloop()

