# coding: utf8
import random

output = []
baseCoeffs = []
coeffs = []
read = []

def main():
    global cryptedMessage
    global text
    for lettre in text:
        lettre = ord(lettre)
        lettre = (lettre + clef) % 126
        output.append(convertBase(lettre))
        read.append(lettre)
    # print("input: ", convertListToNumber(read))
    # print("")
    cryptedMessage = convertListToNumber(output)
    # print("output: ", cryptedMessage)

def getNumber():
    global coeffs
    global baseCoeffs
    number = 0
    for i in range(0, len(baseCoeffs)):
        number = number + (int(coeffs[i]) * int(baseCoeffs[i]))
    return number

def convertBase(message):
    global base
    global baseCoeffs
    global coeffs
    baseCoeffs = []
    coeffs = []

    i = 1
    while pow(base, i) < 126:
        i = i + 1

    for k in range(0, i):
        baseCoeffs.append(pow(base, k))
        coeffs.append(0)

    # c'est là où les problèmes commencent
    while getNumber() != message:
        coeffs[0] = coeffs[0] + 1

        for i in range(0, len(baseCoeffs) - 1):
            if coeffs[i] == base:
                coeffs[i] = 0
                coeffs[i + 1] = coeffs[i + 1] + 1

    coeffs = coeffs[::-1]
    return convertListToNumber(coeffs)

def convertListToNumber(liste):
    number = ""
    for i in liste:
        number += str(i)
    return int(number)

#----------#
#DECRYPTAGE#
#----------#

def decrypt(message): # retourne d'une base inférieure à une base 10
    global messageVisible
    clef = int(input("Clé utilisée pour crypter: "))
    baseDecrypt = input("Base du message à déchiffrer: ")
    nbDeChiffres = 0
    i = 0
    while pow(baseDecrypt, i) < 126:
        i = i + 1

    listeInput = []
    listeOutput = []
    listeBase = []
    message = str(message)
    messagePresqueVisible = []

    for lettre in message:
        if len(listeInput) == i:
            listeOutput.append(calcul(listeInput, baseDecrypt))
            listeInput = []
        listeInput.append(lettre)
    listeOutput.append(calcul(listeInput, baseDecrypt))

    for i in listeOutput:
        messagePresqueVisible.append(chr((i - clef) % 126))
    messageVisible = "".join(messagePresqueVisible)
    print(messageVisible)

def calcul(liste, base):
    number = 0
    liste = liste[::-1]
    for i in range(0, len(liste)):
        number = number + (int(liste[i]) * pow(base, i))
    return number

def StockerTexte(Chaine,NomFichier,Mode):
    with open("/Users/samyhaffoudhi/Desktop/python_projects/CryptoOutput.txt", "w") as Fichier:
        Fichier.write(Chaine)

def SortirTexte():
    with open("/Users/samyhaffoudhi/Desktop/python_projects/CryptoInput.txt", "r") as FichierTexte:
        contenu = FichierTexte.read()
    return contenu

choice = input("Do you want to write a maeesage or to decrypt a message? ")
if choice == "write":
    # text = input("texte à crypter: ")
    text = SortirTexte()
    base = int(input("Quelle base? "))
    clef = input("Clé de cryptage à conserver secrétement: ")
    main()
    StockerTexte(str(cryptedMessage), "CryptoOutput", "w")
elif choice == "decrypt":
    messageSecret = int(SortirTexte())
    decrypt(messageSecret)
    StockerTexte(messageVisible, "CryptoOutput", "w")
else:
    print("Error")
