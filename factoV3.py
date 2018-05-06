from math import sqrt
from collections import Counter
import time

n = int(input("nb a factoriser: "))
sn = int(sqrt(n))
i = 3
p = 0
facteurs=[]

start_time = time.clock()

print("facteurs premiers de n:")

while n%2 == 0:
	facteurs.append(2)
	n = n/2
while n != 1:
	while i <= n and n%i != 0:
		i = i + 2
	facteurs.append(i)
	n = n/i

t = int(len(facteurs))
for i in range(0,t-1):
	print(facteurs[i], "* ", end="")
print(facteurs[-1])

print("finished in", time.clock() - start_time, "seconds")

