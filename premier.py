from math import sqrt

n = 0 #nb a tester
sn = int(sqrt(n))
a = 3
b = "oui"

while b == "oui":
	n = int(input("nb a tester: "))
	if n == 2 or n == 3:
		print("nb premier")
	elif n%2 == 0:
                print("nb non premier")
	else:
		if n%a == 0:
			print("nb non premier")
		else:
			print("nb premier")

		while a <= sn and n%a != 0:
                        a = a+2 

	b = str(input("continuer ? "))



