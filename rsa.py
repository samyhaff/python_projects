import time
from fractions import gcd

# encoding: utf-8
p = int(input("entrez un grand nombre premier p: "))
q = int(input("entrez un grand nombre premier q: "))
n = p * q
pn = (p-1) * (q-1)
e = 0
c = 0

print("n = ", n)
print("phi de n = ", pn)

while gcd(e, pn) != 1:
	while c == 0:
		if ((p < e) and (q < e) and (e < pn)):
			c = 1
		e = e + 1

print("clé publique: ",e,",",n)

msg = raw_input("Phrase à chiffrer: ")
taille_msg = len(msg)
i = 0

while i < taille_msg:
	ascii = ord(mot[i])
	lettre_crypt = pow(ascii, e) % n
	if ascii > n:
		print("p et q trop petits veuillez recommencer")
	elif lettre_crypt > pn:
		print("erreur de calcul")
	print(lettre_crypt)
	i = i+1
