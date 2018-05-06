import math
import random
import itertools

#génération
c = 0
number = [0] * 7
for i in range(0, 7):
    if number.count(0) != 2:
        nb = random.randint(1, 9)
        while number.count(nb) != 0:
            nb = random.randint(1, 9)
        number[i] = nb

number[5] = random.randint(10, 19)
number[6] = random.randint(20, 30)
but = random.randint(500, 1000)

print("Nombre disponibles: ", number)
print("Nombre à deviner: ", but)

#combinaisons
#123 DEBUT
#132 
#312
#321
#231
#213
#123 FIN


    


    
