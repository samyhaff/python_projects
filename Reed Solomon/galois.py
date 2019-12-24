import itertools

p = 2
P = []
irreductible = Polynome.creer([1, 0, 1, 1, 0, 0, 0, 1])
# 100011101

def pgcd(a, b):
    """algorithme d'Euclide"""
    if abs(a) < abs(b):
        return pgcd(b, a)
    while abs(b) > 0:
        q, r = divmod(a, b)
        a, b = b, r
    return a

def euclideEtendu(a, b):
    """algorithme d'euclide étendu"""
    if abs(b) > abs(a):
        (x,y,d) = euclideEtendu(b, a)
        return (y,x,d)
    if abs(b) == 0:
        return (1, 0, a)
    x1, x2, y1, y2 = 0, 1, 1, 0
    while abs(b) > 0:
        q, r = divmod(a,b)
        x = x2 - q * x1
        y = y2 - q * y1
        a, b, x2, x1, y2, y1 = b, r, x1, x, y1, y
    return (x2, y2, a)

class Galois():
    """élement de Z/2Z"""
    def __init__(self, n):
        self.n = n % p

    def __add__(self, other):
        return Galois(self.n + other.n)

    def __sub__(self, other):
        return Galois(self.n + other.n)

    def __mul__(self, other):
        return Galois(self.n * other.n)

    def __truediv__(self, other):
        return self * other.inverse()

    def __div__(self, other):
        return self * other.inverse()

    def __neg__(self):
        return Galois(self.n)

    def __eq__(self, other):
        return self.n == other.n

    def __abs__(self):
        return abs(self.n)

    def __str__(self):
        return str(self.n)

    def __repr__(self):
        return str(self.n)

    def __divmod__(self, diviseur):
        q,r = divmod(self.n, diviseur.n)
        return (Galois(q), Galois(r))

    def inverse(self):
        (x, y, d) = euclideEtendu(self.n, p)
        return Galois(x)

class Polynome():
    """polynome à coeffs dans Z/2Z"""
    def __init__(self, c):
        self.coeffs = c

    @classmethod
    def creer(cls, c):
        return cls([Galois(x) for x in c])

    def estNul(self):
        return self.coeffs == []

    def __repr__(self):
        if self.estNul():
            return "0"
        return ' + '.join(['%s x^%d' % (a,i) if i > 0 else '%s'%a for i,a in enumerate(self.coeffs)])

    def __len__(self):
        return len(self.coeffs)

    def __sub__(self, other):
        return self + other

    def __neg__(self):
        return self

    def coeffDominant(self):
        return self.coeffs[-1]

    def degre(self):
        d = len(self) - 1
        while self.coeffs[d] == Galois(0) and d > 0:
            d -= 1
        return d

    def __eq__(self, other):
        return degre(self) == degre(orther) and all([x==y for (x,y) in zip(self, other)])

    def __add__(self, other):
       c = [a + b for (a, b) in itertools.zip_longest(self.coeffs, other.coeffs, fillvalue = Galois(0))]
       return Polynome(c)

    def __mul__(self, other):
        if self.estNul() or other.estNul():
            return Polynome([])
        c = [Galois(0) for _ in range(len(self) + len(other) - 1)]
        for i, a in enumerate(self.coeffs):
            for j, b in enumerate(other.coeffs):
                c[i + j] += a * b
        return Polynome(c)

    def __divmod__(self, diviseur):
        quotient, reste = Polynome([]), self
        degDiv = diviseur.degre()
        CDdiviseur = diviseur.coeffDominant()

        if degDiv == 0:
            c = diviseur.coeffs[0]
            return Polynome([c.inverse()]) * self, Polynome([])

        while reste.degre() >= degDiv:
            puissanceMonome = reste.degre() - degDiv
            zeros = [Galois(0) for _ in range(puissanceMonome)]
            div = Polynome(zeros + [reste.coeffDominant() / CDdiviseur])
            quotient += div
            reste -= div * diviseur
        return quotient, reste

    def __mod__(self, other):
        return divmod(self * other, irreductible)[1]
