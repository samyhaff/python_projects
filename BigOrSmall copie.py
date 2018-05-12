import random

Solution=random.randint(0,100)
Guess=int(input("Guess: "))

while Guess!=Solution:
    if Guess>Solution:
        print("Too big")
    if Guess<Solution:
        print("Too small")
    Guess=int(input("Guess: "))

print("Nice u found it")
    
