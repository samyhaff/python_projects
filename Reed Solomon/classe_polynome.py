"""Corps de Galois de cardinal 256"""

logTable = [i for i in range(255)]
expTable = [0] * 256
expTable[1] = 0b00000010

def add(x, y):
    return x ^ y

def  soustraction(x, y):
    return add(x, y)

def mul(x,y):
    z = 0
    i = 0
    while (y>>i) > 0:
        if y & (1<<i):
            z ^= x<<i 
        i+=1
    return z

def longueur_bit(n):
    bits = 0
    while n >> bits: bits += 1
    return bits

"""à relire"""
def div(dividend, divisor):
    dl1 = bit_length(dividend)
    dl2 = bit_length(divisor)
    if dl1 < dl2:
        return dividend
    for i in range(dl1 - dl2, -1,- 1):
        if dividend & (1 << i + dl2 - 1):
            dividend ^= divisor << i
    return dividend

def mul_mod(x, y, mod = 0b100011101):
    result = mul(x, y)
    if mod > 0:
        return div(result, mod)
    return result

def creerTableExp(prim = 0b100011101):
    global expTable
    x = 1
    for i in range(2, 255):
        expTable[i] = mulMod(expTable[i - 1], 0b00000010, prim)

def mul2(x, y):
    global logTable
    if x == 0 or y == 0:
        return 0
    a = logTable[x]
    b = logTable[y]
    return expTable(a + b)

def div2(x, y):
    if y == 0:
        raise ZeroDivisionError()
    if x == 0:
        return 0
    return expTable[(logTable[x] + 255 - gf_log[y]) % 255] # on s'assure que l'exposant est positif

def puissance(x, a):
    return expTable[(logTable[x] * power) % 255]

def inverse(x):
    return expTable[255 - logTable[x]]

"""Polynomes"""

class Polynome():

    def __init__(self, coeffs):
        self.coeffs = coeffs

    def polynome_mulScalaire(self, x):
        r = [0] * len(self.coeffs)
        for i in range(0, len(self.coeffs)):
            r[i] = mul2(p[i], x)
        return Polynome(r)

    def __add__(self, q):
        r = [0] * max(len(self.coeffs), len(q.coeffs))
        for i in range(0, len(self.coeffs)):
            r[i+len(r)-len(self.coeffs)] = self.coeffs[i]
        for i in range(0,len(q.coeffs)):
            r[i+len(r)-len(q.coeffs)] ^= q.coeffs[i]
        return Polynome(r)

    def __mul__(self, q):
        r = [0] * (len(self.coeffs)+len(q.coeffs)-1)
        for j in range(0, len(q.coeffs)):
            for i in range(0, len(self.coeffs)):
                r[i+j] ^= mul2(self.coeffs[i], q.coeffs[j]) # equivalent à r[i + j] = add(r[i+j], mul(p[i], q[j]))
        return Polynome(r)

    def eval(self, x):
        y = self.coeffs[0]
        for i in range(1, len(self.coeffs)):
            y = mul2(y, x) ^ self.coeffs[i]
        return y

    def degree(self):
        d = len(self.coeffs) - 1
        while self.coeffs[d] == 0:
            d-=1
        return d

    def div(self, divisor):
        R = self
        B = divisor
        Q = Polynome([])
        while R.degree() >= B.degree():
            d = R.degree() - B.degree() + 1
            C = Polynome([0] * d)
            C.coeffs[-1] = div2(R[-1], B[-1])
            R = R + (B * C)
            Q += C
        return (Q, R)
