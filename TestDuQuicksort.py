import math
import numpy as np
from Fonctions import*
import random
import time

def MotAleatoire():
    Mot=""
    for i in range(6):
        Mot+=Alphabet[random.randint(0,len(Alphabet)-1)]
    return Mot
l = [MotAleatoire() for i in range(10**7)]


debut=time.time()
l.sort()
fin=time.time()

temps=fin-debut

l=" ".join(l)
StockerTexte(l,"TestDuQuicksort","w")

print(temps)
