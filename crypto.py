# coding: utf8

text = input("texte à crypter: ")
base = int(input("Quelle base? "))
output = []
baseCoeffs = []
coeffs = []
read = []

'''

27 = 10 ^ 1 * 2 + 10 ^ 0 * 7

output_string = "".join(list)

97 (base 10) --> base 2

ascii: 0 - 126

1/ trouver n / base ^ n > 126

0 000
1 001
2 010
3 011

'''

def convertNumber():
    global text
    for lettre in text:
        lettre = ord(lettre)
        # print(lettre)
        read.append(lettre)
        output.append(convertBase(lettre))

getNumber():
    global coeffs
    global baseCoeffs
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
        # baseCoeffs = baseCoeffs[::-1]
        coeffs.append(0)

    while getNumber() != lettre:
        for i in range(0, len(coeffs) - 1):
            


convertNumber()
print(baseCoeffs)
print(coeffs)
