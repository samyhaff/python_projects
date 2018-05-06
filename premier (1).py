from math import sqrt
import sys

n = 0 #nb a tester
sn = int(sqrt(n))
a = 3
b = "oui"

while b == "oui":
	n = int(raw_input("nb a tester "))
	if n%2 == 0:
		print("nb non premier")
	else:
		while a <= sn and n%a != 0:
			a = a+2 

		if n%a == 0:
			print("nb non premier")
		else:
			print("nb premier")

	b = str(raw_input("continuer ? "))



