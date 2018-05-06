
from tkinter import Tk, Canvas, PhotoImage, mainloop
from math import sin

WIDTH, HEIGHT = 640, 480

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
canvas.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")
canvas.focus_set()
canvas.bind("<Key>", clavier)
canvas.pack()

for x in range(4 * WIDTH):
    y = int(HEIGHT/2 + HEIGHT/4 * sin(x/80.0))
    img.put("#ffffff", (x//4,y))

window.mainloop()
