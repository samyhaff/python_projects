import random
import numpy
from copy import deepcopy

"""
envoie du message:
1) envoyer la chaine de 0 et de 1
2) attendre confirmation réception de l'arduino
3) envoyer le message
4) balayer les bytes + afficher la lettre correspondante + altéerner la LED

organiser les variables => réduire complexité
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

""" Classe Polybomes """

class Polynomial:

    def __init__(self, coefficients):
        self.coefficients = coefficients
        self.definition=[-10**20,10**20]

    def __repr__(self):
        if self.coefficients==[]:
            return "0"
        liste = []
        if self.coefficients[0]!=0:
            liste.append(str(self.coefficients[0]))
        for degre,coefficient in enumerate(self.coefficients[1:],1):
            if coefficient!=0:
                liste.append(str(coefficient) + "X^" + str(degre))
        liste.reverse()
        text = "+".join(liste)
        text = text.replace("+-","-").replace("1X","X")
        return text

    def adapt(self,coefficients,size):
        coefficients += [0]*(size-len(coefficients))
        return coefficients

    def __add__(self, other):
        maxdegree = max(self.degree()+1,other.degree()+1)
        cA = self.adapt(self.coefficients,maxdegree)
        cB = self.adapt(other.coefficients,maxdegree)
        newcoefficients = [(a + b) % 2 for (a,b) in zip(cA, cB)]
        A=Polynomial(newcoefficients)
        A.correct()
        return A

    def __sub__(self, other):
        # return self+other*Polynomial([-1])
        return self + other

    def __mul__(self, other):
        degree = len(self.coefficients) + len(other.coefficients)
        A = self.coefficients + [0]*(degree-len(self.coefficients)+1)
        B = other.coefficients + [0]*(degree-len(other.coefficients)+1)
        newcoefficients = []
        for k in range(degree + 1):
            coeff = 0
            for i in range(k + 1):
                coeff += A[i] * B[k - i]
            newcoefficients.append(coeff)
        C = Polynomial(newcoefficients)
        C.correct()
        return C

    def correct(self):
        """Correct the coefficients of the polynomial by deleting useless zeros at the end,"""
        while len(self.coefficients)>1:
            if self.coefficients[-1] == 0:
                del self.coefficients[-1]
            else:
                break
        if self.coefficients==[0]:
            self.coefficients=[]
        """and then replace float coefficients by int coefficients if possible."""
        for i in range(len(self.coefficients)):
            if self.coefficients[i]==int(self.coefficients[i]):
                self.coefficients[i]=int(self.coefficients[i])

    def __len__(self):
        A=deepcopy(self)
        A.correct()
        return len(A.coefficients)-1

    def degree(self):
        A=deepcopy(self)
        A.correct()
        return len(A.coefficients)-1

    def __getitem__(self,index):
        return self.coefficients[index]

    def __setitem__(self,index,value):
        self.coefficients[index] = value

    def __delitem__(self,index):
        del self.coefficients[index]

    def derivate(self):
        self.coefficients = [i*c for (i,c) in enumerate(self.coefficients)]
        del self.coefficients[0]

    def derivative(self):
        newcoefficients = [i*c for (i,c) in enumerate(self.coefficients)]
        del newcoefficients[0]
        return Polynomial(newcoefficients)

    def unit(self):
        k=self.coefficients[-1]
        newcoefficients=[]
        for i in range(len(self.coefficients)):
            newcoefficients.append(self.coefficients[i]/k)
        A=Polynomial(newcoefficients)
        A.correct()
        return A

    def unitarize(self):
        """Convert the polynomial into its unit form."""
        self=self.unit()

    def __xor__(self,other):
        """Return the HCF (PGCD  en francais) of self and other by Euclide algorithm. Make use of "^" operator."""
        R0 = deepcopy(self)
        R1 = deepcopy(other)
        R0.correct()
        R1.correct()
        listR=[R0,R1]
        while listR[-1].degree()>0:
            R,Q=listR[-2]/listR[-1]
            listR.append(R)
        return listR[-2]

    def __truediv__(self, other):
        R = deepcopy(self)
        B = deepcopy(other)
        R.correct()
        B.correct()
        Q = Polynomial([])
        while R.degree() >= B.degree():
            d = R.degree() - B.degree() + 1
            C = Polynomial([0 for i in range(d)])
            C[-1] = R[-1] // B[-1]
            R = R - B * C
            Q = Q + C
        return (Q, R)

    def __call__(self,x):
        """Evaluate the polynomial given an x value."""
        sum=0
        for n,c in enumerate(self.coefficients):
            sum+=c*x**n
        return sum

    def allDerivatives(self):
        B=deepcopy(self)
        derivatives=[deepcopy(self)]
        while B.degree()>1:
            B.derivate()
            derivatives.append(deepcopy(B))
        return derivatives

    def roots(self):
        roots=[]
        derivatives=self.allDerivatives()
        print(derivatives)
        derivatives.reverse()
        old_extrema=[]
        for derivative in derivatives:
            new_extrema=[]
            neglim=self.definition[0]
            poslim=self.definition[1]
            extrema=[neglim]+old_extrema+[poslim]
            for i in range(len(extrema)-1):
                if derivative(extrema[i])*derivative(extrema[i+1])<=0:
                    new_extrema.append(derivative.gradientDescent(extrema[i],extrema[i+1]))
            old_extrema=new_extrema[:]
        return new_extrema

    def gradientDescent(self,xa,xb,precision=10e-10):
        if self(xa)*self(xb)>0:
            raise Exception
        a=min(xa,xb)
        b=max(xa,xb)
        x=(a+b)/2
        while abs(self(x))>precision:
            if self(x)*self(b)>0:
                b=x
            if self(x)*self(a)>0:
                a=x
            x=(a+b)/2
        return x

def creePolynome(chaine):
    """ marche seulement pour les polynomes à coeffs valant 0 ou 1 """
    coeffs = [0] * (int(chaine[2]) + 1)
    if chaine[-1] == "1":
        coeffs[-1] = 1
    for k in range(len(chaine) - 2):
        if chaine[k] == "X":
            coeffs[len(coeffs) - 1 - int(chaine[k + 2])] = 1
    return coeffs

""" main """

chaine = "Hello, World!"
message = ""
for c in chaine:
    x = toBin(ord(c))
    message += ''.join(str(x)) # chaine envoyée en binaire
messageRecu = simulationErreurs(2) # chaine reçue en binaire
chaineRecue = toStr() # chaine reçue en lettres
listeMessageEnvoye = []
listeMessageRecu = []
for c in message:
    listeMessageEnvoye.append(int(c)) # chaine envoyée en liste
for c in listeMessageRecu:
    listeMessageRecu.append(int(c))

"""
DEBUG:
print(message)
print(chaine)
print(listeMessageEnvoye)
print(messageRecu)
print(chaineRecue)
print(listeMessageRecu)

polynomeEnvoye = Polynomial(listeMessageEnvoye[::-1])
print(Polynomial([0,0,1,0,1,0,1,1]) / Polynomial([0,1,0,1,1]))
generateur = Polynomial()
"""

print(creePolynome("X^3+X^2+1"))
