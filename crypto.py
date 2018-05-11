# coding: utf8

messageSecret = int(input("Votre message: "))
# text = input("texte à crypter: ")
# base = int(input("Quelle base? "))
output = []
baseCoeffs = []
coeffs = []
read = []

def main():
    global cryptedMessage
    global text
    for lettre in text:
        lettre = ord(lettre)
        output.append(convertBase(lettre))
        read.append(lettre)
    print("input: ", convertListToNumber(read))
    print("")
    cryptedMessage = convertListToNumber(output)
    print("output: ", cryptedMessage)

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

def decrypt(message): # retourne d'une base inférieure à une base 10
    baseDecrypt = input("Base du message à déchiffrer: ")
    nbDeChiffres = 0
    i = 0
    while pow(baseDecrypt, i) < 126:
        i = i + 1
    # print(i, " lettres par bloc")

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
        print(listeInput)
        print(len(listeInput))
    listeOutput.append(calcul(listeInput, baseDecrypt))

    for i in listeOutput:
        messagePresqueVisible.append(chr(i))
    messageVisible = "".join(messagePresqueVisible)
    print(messageVisible)

def calcul(liste, base):
    number = 0
    liste = liste[::-1]
    for i in range(0, len(liste)):
        number = number +(int(liste[i]) * pow(base, i))
    return number

# main()
decrypt(messageSecret)
