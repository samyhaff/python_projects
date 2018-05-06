import random

list_a = []
list_b = []
list_c = []

with open("insults.csv", "r") as f:
    for line in f:
        words = line.split(",")
        list_a.append(words[0])
        list_b.append(words[1])
        list_c.append(words[2].strip())

def insult_me():
    word_a = random.choice(list_a)
    word_b = random.choice(list_b)
    word_c = random.choice(list_c)
    insult = "Thou" + " " + word_a + " " + word_b + " " + word_c
    print(insult)

nb = input("How many insults do you want? ")
for i in range(0, int(nb)):
    insult_me()
