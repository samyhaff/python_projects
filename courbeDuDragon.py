import mathplotlib.pyplot as plt

a, b = 0, 1 # coordonnées initiales

def courbeDuDragon(n):
    x = [a]
    y = [b]
    for _ in range(n):
        for i in range(0, len(x)):
            x = x[0:i] + (x[i] + [x[i + 1] / 2] + x[i:len(x)]
