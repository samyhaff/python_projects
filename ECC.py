import random
import numpy

"""

envoie du message:
1) envoyer la chaine de 0 et de 1
2) attendre confirmation réception de l'arduino
3) envoyer le message
4) balayer les bytes + afficher la lettre correspondante + altéerner la LED

"""

""" transmission """

def toBin(n):
    bin = []
    while n // 2 > 0 or len(bin) < 8:
        bin.append(n % 2)
        n = n // 2
    bin.reverse()
    return ''.join(str(c) for c in bin)

def simulationErreurs(n):
    if n == 0:
        return message
    indices = random.sample([i for i in range(0, len(message))], n)
    result = ""
    for i in range(0, len(message)):
        if indices.count(i) > 0:
            result += str((int(message[i]) + 1) % 2)
        else:
            result += message[i]
    return result

def toDecimal(n):
    output = 0
    for i in range(0, len(n)):
        output += int(n[i]) * (2 ** (7 - i))
    return output

def toStr():
    output = ""
    n = len(messageRecu) // 8
    for i in range(0, n):
        output += chr(int(toDecimal(messageRecu[8 * i : 8 * (i + 1) + 1])))
    return output

def distanceHamming(a, b):
    s = 0
    n = len(a)
    for i in range(n):
        if a[i] != b[i]:
            s += 1
    return s

chaine = "Hello, World!"
message = ""
for c in chaine:
    message += ''.join(str(toBin(ord(c))))
messageRecu = simulationErreurs(2)
chaineRecue = toStr()

print(message)
print(chaine)
print(messageRecu)
print(chaineRecue)

""" Classe Polybomes """

class Polynome:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __repr__(self):
        liste = []
        if self.coefficients[0]!=0:
            liste.append(str(self.coefficients[0]))
        for degre,coefficient in enumerate(self.coefficients[1:],1):
            if coefficient!=0:
                liste.append(str(coefficient) + "X^" + str(degre))
        liste.reverse()
        text="+".join(liste)
        text=text.replace("^1","").replace("+-","-").replace("1X","X")
        return text

    def adapt(self,liste,degree):
        #Return a liste of coefficients of the right degree by adding zeros at the end
        liste+=[0]*(degree-len(liste))
        return liste

    def __add__(self, other):
        degree=max(len(self.coefficients),len(other.coefficients))
        A=self.adapt(self.coefficients,degree)
        B=self.adapt(other.coefficients,degree)
        #A,B=self.adapt(self.coefficients,other.coefficients)
        newcoefficients=[a+b for (a,b) in zip(A, B)]
        return Polynome(newcoefficients)

    def __mul__(self, other):
        #A,B=self.adapt(self.coefficients,other.coefficients)
        deg = len(self.coefficients) + len(other.coefficients)
        A = self.coefficients + [0]*(deg-len(self.coefficients)+1)
        B = other.coefficients + [0]*(deg-len(other.coefficients)+1)
        print(A,B)
        newcoefficients = []
        for k in range(deg + 1):
            coeff = 0
            for i in range(k + 1):
                coeff += A[i] * B[k - i]
            newcoefficients.append(coeff)
        #newcoefficients=[e for e in newcoefficients if ]
        newcoefficients=self.correct(newcoefficients)
        return Polynome(newcoefficients)

    def correct(self,liste):
        while liste[-1] == 0:
            del liste[- 1]
        return liste

    def division(self, B):


""" Reed Solomon """
