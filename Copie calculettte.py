from tkinter import *
import math
import random

Width = 5
Height = 20

Liste1=[0]*5
Liste2=[0]*5
L3=[0,1,1,1,1,1,1,0]

w=Width
h=Height



window = Tk()
canvas = Canvas(window, width=Width, height=Height, bg="#ffffff")
canvas.pack()
img = PhotoImage(width=Width, height=Height)
canvas.create_image((Width/2, Height/2), image=img, state="normal")


a=0

y=10
img.put("#000000", (2,y))
Liste2[2]=1

while y<=10+5:
    y=y+1
    x=1
    r=3
    Liste1=Liste2
    print(Liste1)
    while x<=r:
        i=x
        Liste2[i]=1
        if Liste1[i-1]==0 and Liste1[i]==0 and Liste1[i+1]==0:
            Liste2[i]=0

        if Liste1[i-1]==1 and Liste1[i]==0 and Liste1[i+1]==1:
            print("ça fonctionne")

        a=Liste1[i-1]+2*Liste1[i]+4*Liste1[i+1]
        
        if a==7:
            print(Liste1[2])
            Liste2[i]=0
            print(Liste1[2])
        
        if Liste2[i]==1:
            img.put("#000000", (x,y))


        
        x=x+1
mainloop()

