from math import sqrt
import sys

Nombre = int(input("Nombre = "))
Debut = "Vrai"
Puissance = 0
AncienDiviseur = 0

if Nombre <= 1:
    print("Le nombre est invalide")
else:
    for Diviseur in range(2,4):
        Puissance = 0
        while Nombre%Diviseur == 0:
            Puissance = Puissance + 1
            if AncienDiviseur != Diviseur:
                if Debut == "Vrai":
                    Debut = "Faux"
                else:
                    print('*',end=" ")
                print(Diviseur,end=" ")
            else:
                if Puissance == 2:
                    print('^',end=" ")
            Nombre = Nombre/Diviseur
            AncienDiviseur = Diviseur
        if Puissance >= 2:
            print(Puissance,end=" ")

    Diviseur = 5

    while Nombre != 1:
        Puissance = 0
        while Nombre%Diviseur != 0:
            Diviseur = Diviseur+2
        while Nombre%Diviseur == 0:
            Puissance = Puissance + 1
            if AncienDiviseur != Diviseur:
                if Debut == "Vrai":
                    Debut = "Faux"
                else:
                    print('*',end=" ")
                print(Diviseur,end=" ")
            else:
                if Puissance == 2:
                    print('^',end=" ")
            Nombre = Nombre/Diviseur
            AncienDiviseur = Diviseur
        if Puissance >= 2:
            print(Puissance,end=" ")
