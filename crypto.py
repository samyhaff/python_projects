# coding: utf8

# text = input("texte à crypter: ")
base = int(input("Quelle base? "))
output = []
baseCoeffs = []
coeffs = []
retenue = []
read = []



def main():
    global text
    for lettre in text:
        lettre = ord(lettre)
        # print(lettre)
        read.append(lettre)
        output.append(convertBase(lettre))

def getNumber(): # nombre à tester
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
    # global retenue

    i = 1
    while pow(base, i) < 126:
        i = i + 1

    for k in range(0, i):
        baseCoeffs.append(pow(base, k))
        # retenue.append[0]
        coeffs.append(0)

    print(coeffs)
    print(baseCoeffs)

    # c'est là où les problèmes commencent
    while getNumber() != message:

        coeffs[0] = coeffs[0] + 1

        for i in range(0, len(baseCoeffs) - 1):
            if coeffs[i] == base:
                coeffs[i] = 0
                coeffs[i + 1] = coeffs[i + 1] + 1

        print(coeffs)

        '''
        if coeffs[0] < base - 1:
            coeffs[0] = coeffs[0] + 1
        else:
            # retenue[1] = 1
            coeffs[0] = 0
            coeffs[1] = (coeffs[1] + 1)

        for i in range(1, len(coeffs) - 1):
            if coeffs[i] == base - 1:
                coeffs[i] = 0
                coeffs[i + 1] = coeffs[i + 1] + 1
        '''


'''
26 = 11010
0000000
0000001
...
0000009
0000010
...
0000019
0000020


'''

# main()

convertBase(64)
print(baseCoeffs)
print(coeffs)
