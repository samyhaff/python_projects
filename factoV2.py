from math import sqrt

n = input("n = ") #nb a factoriser
d = 2 

while d <= sqrt(n):
	while (n%d) != 0 and d <= sqrt(n):
        	d = d+1
	if d <= sqrt(n):
		n = n/d
		print(d)
print(n)
