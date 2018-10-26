taille = 400
pas = taille // 10
openSet = []
closedSet = []
obstacles = []
path = []
parents = []
count = 0
x = -1
y = -1
r, v, b = 0, 0, 0
canClick = 1

def setup():
    size(taille, taille)
    background(255, 255, 255)
    strokeWeight(2)
    stroke(0)

def mousePressed():
    global canClick
    global count
    global x
    global y
    global r
    global v
    global b
    global goal
    global s
    x = mouseX
    y = mouseY
    node = (x // pas, y // pas)
    if mouseButton == RIGHT:
        canClick = 0
    if count == 0:
        count += 1
        r = 0
        v = 255
        b = 0
        s = (node)
        openSet.append(s)
    elif count == 1:   
        count += 1
        r = 255
        v = 0
        b = 0
        goal = (node)
    elif canClick == 1:
        r = 0
        v = 0
        b = 0
        obstacles.append(node)

def getF((x, y)):
    global s
    global goal
    h = abs(x - goal[0]) + abs(y - goal[1])
    g = abs(x - s[0]) + abs(y - s[1])
    return h + g

def getLowest():
    global s
    global openSet
    lowestF = int(taille * sqrt(2) // pas)
    lowest = (0, 0)
    for node in openSet:
        if getF(node) < lowestF:
            lowestF = getF(node)
            lowest = node
    return lowest

def reachedGoal():
    global goal
    if getLowest() == goal:
        return True
    return False

def valid(x, y):
    if x <= taille // pas and x >= 0 and y <= taille // pas and y >= 0:
        return True
    return False

def getNeighboors((x, y)):
    global neighboors
    neighboors = []
    if valid(x - 1, y):
        neighboors.append((x - 1, y))
    if valid(x + 1, y):
        neighboors.append((x + 1, y))
    if valid(x, y - 1):
        neighboors.append((x, y - 1))
    if valid(x, y + 1):
        neighboors.append((x, y + 1))    

def g((x, y)):
    return abs(x - s[0]) + abs(y - s[1])

def D((x, y), (i, j)):
    return abs(x - i) + abs(y - j)

def draw():   
    global count
    global x 
    global y
    global r
    global v
    global b
    global closedSet
    global openSet
    global parents
    global canClick

    for i in range(pas, taille, pas):
        line(i, 0, i, taille) 
        line(0, i, taille, i)

    fill(r, v, b)
    ix = x // pas
    iy = y // pas
    rect(ix * pas, iy * pas, pas, pas)
    
    if canClick == 0:
        while not reachedGoal():
            current = getLowest
            closedSet.append(current)
            getNeighboors(current)
            for node in neighboors:
                cost = g(current) + D(current, neighboor)
                if openSet.count(neighboor) > 0 and cost < g(neighboor):
                    openSet.remove(neighboor) # path is better
                if closedSet.count(neighboor) > 0 and cost < g(neighboor):
                    closedSet.remove(neighboor)
                if openSet.count(neighboor) == 0:
                    gNeighboor = cost
                    openSet.append(neighboor)
                    
                    parents.append((cuurent, neighboor))
                    
