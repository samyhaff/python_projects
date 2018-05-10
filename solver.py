import math
import random

#---------#
#Variables#
#---------#

signes="+-*^/="
minVariables="abcdefghijklmnopqrstuvwxyz"
majVariables="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nombresL="0123456789"

#----------#
#Brouillons#
#----------#

'''

read
[17,"x","+",7,"+",15,"=",0]
reduire
[17,"x","+",22,"=",0]

5x+3=7x+7

5x+7x=3+7

12x=10

12x-10=0

[17,"x","+",7,"=",0]
theoriser
[A,a,"+",B,"=",C]

[A,a,"=",B]


[A,a,"+",B,"=",C]
#objectif samy
[A,a,"+",B,"=",0]




[A,a,"^",B,"+",C,"=",0]


[A,a,"=",B]


[A,a,"^",B+D"="0"]

'''

#---------#
#Fonctions#
#---------#

def main(equation):
    global listeSol
    equation=supprimerEspace(equation)
    global liste=read(equation)
    modele=theoriser(liste)
    resoudre(modele)
    print(equation)


def lecture(equation):
    listeInit=[]
    for lettre in equation:
        if lettre in nombres:
            listeInit.append(int(lettre))
        else:
            listeInit.append(lettre)
    i=0
    fini=False
    while fini==False:
        fini=True
        for lettre in listeInit:
            if i+1<len(listeInit):
                if type(lettre)==int and type(listeInit[i+1])==int:
                    lettre2=int(lettre)*10+(listeInit[i+1])
                    del listeInit[i]
                    listeInit[i]=lettre2
                    fini=False
            i+=1
    return listeInit

def simplificationSignes(equation):
    nerienfaire=0
    return "wesh"


def theoriser(liste):
    global nombresL
    indiceNombre=0
    indiceVariable=0
    theorie=[]
    for term in liste:
        if type(term)==int:
            if term!=0:
                theorie.append(majVariables[indiceNombre])
                indiceNombre+=1
        elif minVariables.count(term)==1:
            theorie.append(minVariables[indiceVariable])
            indiceVariable+=1
        else:
            theorie.append(term)
    return theorie

def valide(equation):
    for lettre in equation:
        if lettre == "=":
            return True
    return False


#if liste=[A,a,"+",B,"=",C]
    #if liste = [A,a,"+",B,"=",0]
        #nombre=>soluce

#liste=[A,a,"+",B,"=",C] and nombre=[1,2,3]
#sortie=[Aa+]

machin=ordonner(liste,nombre)

def ordonner(nombres):
    global liste
    reels=[]
    coeffs=[]
    if majVariables.count(liste[0])=1 and signes.count(liste[0])=1:
        reels.append(liste[0])
    if signes.count(liste[-1])=1 and majVariables.count(liste[-1])=1:
        reels.append(liste[-1])
    for i in range(1,len(liste)-1):
        if signes.count(liste[i-1])=1 and majVariables.count(liste[i])=1 and signes.count(liste[i+1])=1:
            reels.append(liste[i])
    for reel in range(len(reels)):
        if nombres.count(reel)==1:

# signes possibles: + - / x

def simplifier():
    operation = [0] # opérations à droite
    sommes = [] # somme des nombres à droite
    somme = 0
    global liste
    global nombres
    global signes

    i = 0
    for lettre in liste:
        if lettre == "=":
            for k in range(i, len(liste)):
                if signes.count(liste[k]) == 0:
                    somme.append(liste[k])
                    if signes.count(liste[k - 1]) > 0 and liste[k] != "=":
                        operation.append(liste[k])
            del liste[i : len(liste) - 1]

        i+=1

    for j in range(0, somme.len()):
        if operation[j] == "+":
            somme = somme + somme[j]
        if operation[j] == "-":
            somme = somme - somme[j]
        if operation[j] == "/":
            somme = somme / somme[j]
        if opération[j] == "*":
            somme = somme * somme[j]
        if operation[j] == 0:
            somme = somme[j]
    liste.append(somme)

def resoudre(modele):
    [1,3]
    global listeSol=[]
    if modele == ["A","a","+","B","=","0"]:
        solution=resoudreAffine(liste,nombres)
        listeSol.append(solution)
    if liste == ["A","a","^","B","+","C","c","+","D","=","0"]:
        nerienfaire=0

def resoudreAffine(liste):
    A = float(nombres[0])
    B = float(nombres[1])
    solution = - B / A
    return solution

#ne sert a rien
def simplifier():
    global liste
    global nombres
    if liste == ["A","a","+","B","=","C"]:
        liste = ["A","a","+","B","=","0"]
        nombres[1] = nombres[1] - nombres[2]
        del nombres[2]

def supprimerEspace(equation):
    for indice in range(len(equation)):
        if equation[indice]==" ":
            del equation[indice]
    return(equation)

#-------#
#Actions#
#-------#

str(equation)=input("Equation: ")
main(equation)
print("La liste solution est: ",listeSol)
