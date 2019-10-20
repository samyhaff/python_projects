import numpy as np

pi = np.pi

class Quaternion():

    def __init__(self, coeffs):
        self.a = coeffs[0]
        self.b = coeffs[1]
        self.c = coeffs[2]
        self.d = coeffs[3]
        self.v = coeffs[1:] # vecteur u(b, d, c)

    @classmethod
    def vect(cls, a, v):
        return cls([a, v[0], v[1], v[2]])

    @classmethod
    def angle(cls, angle, v):
        s = np.sin(angle / 2)
        return cls([np.cos(angle / 2), s * v[0], s * v[1], s * v[2]])

    def __repr__(self):
        return (str(self.a) + " + " + str(self.b) + "i + " + str(self.c) + "j + " + str(self.d) + "k")

    def __neg__(self):
        return Quaternion([-self.a, -self.b, -self.c, -self.d])

    def __abs__(self):
        return np.sqrt(self.a ** 2 + self.b ** 2 + self.c ** 2 + self.d ** 2)

    def conjugate(self):
        return Quaternion([self.a, -self.b, -self.c, -self.d])

    def __add__(self, other):
        return Quaternion([self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d])

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return Quaternion([self.a*other.a-self.b*other.b-self.c*other.c-self.d*other.d,
                          self.a*other.b+self.b*other.a+self.c*other.d-self.d*other.c,
                          self.a*other.c+self.c*other.a+self.d*other.b-self.b*other.d,
                          self.a*other.d+self.d*other.a+self.b*other.c-self.c*other.b])

    def __truediv__(self, other):
        t = self * other.conjugate()
        m = abs(other) ** 2
        return Quaternion([t.a / m, t.b / m, t.c / m, t.d / m])

    def __eq__(self, other):
        return (self.a == other.b and self.b == other.b and self.c == other.c and self.d == other.d)

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return (str(self.a) + " + " + str(self.b) + "i + " + str(self.c) + "j + " + str(self.d) + "k")

    def __invert__(self):
        t = self.conjugate()
        m = abs(self) ** 2
        return Quaternion([t.a / m, t.b / m, t.c / m, t.d / m])

q1 = Quaternion([1,0,0,0])
q2 = Quaternion([1,1,1,1])
print(q1 * ~q1)
