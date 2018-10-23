def setup():
    size(400, 120)
    background(255)
    
def draw():
    stroke(255, 0, 0)
    line(150,25,mouseX,mouseY)
    println("x: " + str(mouseX) + " y: " + str(mouseY))
    
def mousePressed():
    background(255)
    
