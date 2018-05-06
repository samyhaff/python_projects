from tkinter import *
import math
import random

Width = 640
Height = 400

window = Tk()
canvas = Canvas(window, width = Width, height = Height, bg = "#000000")
canvas.pack()
img = PhotoImage(width = Width, height = Height)
canvas.create_image(Width // 2, Height // 2, image = img, state = "normal")

#for x in range(Width):
#       for y in range(Height):
#               img.put("#ffffff", (x, y))

while 1 == 1 :
        y = random.randint(0, Height)
