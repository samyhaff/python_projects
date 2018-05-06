from tkinter import *
import math
import random
import time

Width=200
Height=200

def clavier(event):
    touche=event.keysym
    print(touche)
    
fenetre=Tk()

canvas = Canvas(fenetre, width=Width, height=Height, bg="#ffffff")
canvas.focus_set()
canvas.bind("<Key>", clavier)
canvas.pack()

fenetre.mainloop()
