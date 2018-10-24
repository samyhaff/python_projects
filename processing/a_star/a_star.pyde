taille = 400
pas = taille // 20

def setup():
    size(taille, taille)
    background(255, 255, 255)
    strokeWeight(2)
    stroke(0)

count = 0
x = -1
y = -1
r, g, b = 0, 0, 0
canClick = 1

def mousePressed():
    global canClick
    global count
    global x
    global y
    global r
    global g
    global b
    if mouseButton == RIGHT:
        canClick = 0
        print("phase initiale términée, passons aux choses sérieuses")
    if count == 0:
        x = mouseX
        y = mouseY    
        count += 1
        r = 0
        g = 255
        b = 0
    elif count == 1:
        x = mouseX
        y = mouseY    
        count += 1
        r = 255
        g = 0
        b = 0
    elif canClick == 1:
        x = mouseX
        y = mouseY
        r = 0
        g = 0
        b = 0

def draw():   
    global count
    global x 
    global y
    global r
    global g
    global b

    for i in range(pas, taille, pas):
        line(i, 0, i, taille) 
        line(0, i, taille, i)

    fill(r, g, b)
    ix = x // pas
    iy = y // pas
    rect(ix * pas, iy * pas, pas, pas)
