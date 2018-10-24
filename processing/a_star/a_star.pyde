taille = 400
pas = taille // 20

def setup():
    size(taille, taille)
    background(255, 255, 255)
    strokeWeight(2)
    stroke(0)

enter_x = -1
enter_y = -1

def mousePressed():
    global enter_x, enter_y
    if enter_x < 0 or enter_y < 0:
        enter_x = mouseX
        enter_y = mouseY    

def draw():   
    global enter_x, enter_y

    for i in range(pas, taille, pas):
        line(i, 0, i, taille) 
        line(0, i, taille, i)

    if enter_x >= 0 and enter_y >= 0:
        fill(0, 255, 0)
        ix = enter_x // pas
        iy = enter_y // pas
        rect(ix * pas, iy * pas, pas, pas)
