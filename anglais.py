import random
liste = []
n = int(input("nombre de mots: "))
for a in range(1, n + 1):
    liste.append(a)
qts = []
i= 0
mot = random.randint(1, n)
r = n

while True:
    while qts.count(mot) != 0:
        mot = random.randint(1, n)
    qts.append(mot)
    print(mot)
    k = input("connaissez vous ce mot? ")
    if k == "n":
        qts.remove(mot)
        r = r + 1
    r = r - 1
    print(r, "mots restants")
print("Vous connaissez vos mots, vous etes trop chaud")
        


