taille = 400
pas = taille // 20
canDraw = True
def setup():
    size(taille, taille)
    background(255, 255, 255)
    stroke(0)
    strokeWeight(2)
    fill(0)
    
def draw():
    global canDraw
    for i in range(pas, taille, pas):
        line(i, 0, i, taille)
        line(0, i, taille, i)
    if mousePressed:
        if mouseButton == RIGHT:
            canDraw = False
            
    if canDraw == True:
        if mousePressed:
            x = mouseX
            y = mouseY
            for i in range(1, taille // pas - 1):
                for j in range(1, taille // pas - 1):
                    if i * pas <= x and x <= (i + 1) * pas:
                        if j * pas <= y and y <= (j + 1) * pas:
                            rect(i * pas, j * pas, pas, pas)
    
    
