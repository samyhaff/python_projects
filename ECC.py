import random
import numpy
from copy import deepcopy
import serial

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
    """Class that makes polynomials."""

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
        newcoefficients = [a ^ b for (a,b) in zip(cA, cB)]
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
            sum = add(sum, mul(c, power(x, n)))
        return sum


""" CORPS FINIS DE CARDINAL 256 """

def creePolynome(chaine):
    """ marche seulement pour les polynomes à coeffs valant 0 ou 1 """
    coeffs = [0] * (int(chaine[2]) + 1)
    if chaine[-1] == "1":
        coeffs[-1] = 1
    for k in range(len(chaine) - 2):
        if chaine[k] == "X":
            coeffs[len(coeffs) - 1 - int(chaine[k + 2])] = 1
    return Polynomial(coeffs)

def add(x, y):
    return x ^ y

def sub(x, y):
    return add(x, y)

def mul(x,y):
    z = 0
    i = 0
    while (y>>i) > 0:
        if y & (1<<i):
            z ^= x<<i
        i += 1
    return z

def bit_length(n):
    bits = 0
    while n >> bits: bits += 1
    return bits

def div(dividend, divisor=None):
    dl1 = bit_length(dividend)
    dl2 = bit_length(divisor)
    if dl1 < dl2:
        return dividend
    # Else, align the most significant 1 of the divisor to the most significant 1 of the dividend (by shifting the divisor)
    for i in range(dl1-dl2,-1,-1):
        # Check that the dividend is divisible (useless for the first iteration but important for the next ones)
        if dividend & (1 << i+dl2-1):
            # If divisible, then shift the divisor to align the most significant bits and XOR (carry-less subtraction)
            dividend ^= divisor << i
    return dividend

def power(x, p):
    if p == 0:
        return 0b00000001
    if p == 1:
        return x
    return mul(x, pow(x, p - 1))

def rs_generator_poly(nsym):
    g = Polynomial([1])
    for i in range(0, nsym):
        g = g * Polynomial([1, power(0b00000010, i)])
    return g

def rs_encode_msg(msg_in, nsym):
    '''Reed-Solomon main encoding function'''
    gen = rs_generator_poly(nsym)
    _, remainder = msg_in / gen
    msg_out = msg_in + remainder
    return msg_out

def rs_calc_syndromes(msg, nsym):
    synd = Polynomial([0] * nsym)
    for i in range(0, nsym):
        synd[i] = msg.call(power(0b00000010,i))
    return Polynomial([0] + synd.coefficients()) # pad with one 0 for mathematical precision (else we can end up with weird calculations sometimes)

def rs_loc(e_pos):
    e_loc = Polynomial([1])
    for i in e_pos:
        e_loc = e_loc * (Polynomial([1]) + Polynomial[power(0b00000010, i), 0])
    return e_loc

""" MAIN """

chaine = "Bonjour!"
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

"""

polynomeMessage = Polynomial(listeMessageEnvoye[::-1])
generateur = creePolynome("X^16+X^12+X^5=1") # détecte les erreurs pour 2 bits tant que les puissances éloignées de au plus 32k
polynomeTransmission = polynomeMessage - (polynomeMessage / generateur)[1]
