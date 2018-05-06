from tkinter import *
import math

def clavier(event):
    touche = event.keysym
    if touche=="Return":
        print("Je suis génial")

fenetre = Tk()
canvas = Canvas(fenetre, width=500, height=500)
canvas.focus_set()
canvas.bind("<Key>", clavier)
canvas.pack()

fenetre.mainloop()

