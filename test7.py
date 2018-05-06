import math
import numpy
import pickle
from Fonctions import *

Mot="osef"
while Mot!="stop":
    Mot=input("Chercher le nombre de syllables du mot: ").lower()
    print("Ce mot a",Syllables(Mot),"syllables.")
    print("")
