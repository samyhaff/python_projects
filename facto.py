from math import sqrt

n = input("n = ") #nb a factoriser
d = 2 #1ier diviseur
e=1 #2eme diviseur
f=2 #diviseur de e

while (n%d) != 0 and d <= sqrt(n):
	d = d+1

if (n%d) != 0 and n != 2:
	print("nb non factorisable")
else:
	e = n/d
	while e%f != 0 and f <= sqrt(e):
		f = f+1
	if (e%f) != 0:
		print("n=",d,"*",f)
	else:
		print("n=",d,"*",e)
