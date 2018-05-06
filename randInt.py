import math
import random

n = int(input("combien de chiffres? "))
s = input("nombre binaire? ")

if s == "non":
	d = int(random.randint(1,9))
	print("Nombre aleatoire:")
	print(d,end="")
	for i in range(2,n):
		d = random.randint(0,9)
		print(d,end="")
	if n>1:
		d = random.randint(1,9)
		print(d)
if s == "oui":
        print("Nombre aléatoire:")
       	print(d,end="")
    	for j in range(1,n):
		d = random.randint(0,1)
             	print(d,end="")
        if n>1:
                d = random.randint(0,1)
                print(d)

