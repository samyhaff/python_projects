from tkinter import *
import math
import random

w = 1000
h = 500

x = w // 2
y = 10

a = 0
b = 0
c = 0

l1 = [0] * w
l2 = [0] * w
l3 = [0,1,1,1,1,0,0,0] 
l1[int(w/2)] = 1

window = Tk()
canvas = Canvas(window, width = w, height = h, bg = "#ffffff")
canvas.pack()
img = PhotoImage(width = w, height = h)
canvas.create_image(w // 2, h // 2, image = img, state = "normal")

img.put("#000000", (x, y))
        
for y in range(11, h):
    for x in range(1, w-1):
        for c in range(0, 2):
            for b in range(0, 2):
                for a in range(0, 2):
                    if l1[x-1] == a and l1[x] == b and l1[x+1] == c :
                        l2[x] = l3[a + 2 * b + 4 * c]
        if l2[x] == 1:
            img.put("#000000", (x,y))
    l1 = l2[:]
    
window.mainloop()
