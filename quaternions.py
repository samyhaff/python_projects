import numpy as np

class Quaternion():

    def __init__(self, coeffs):
        self.a = coeff[0]
        self.b = coeff[1]
        self.c = coeff[2]
        self.d = coeff[3]
        self.v = coeffs[1:] # vecteur u(b, d, c)

    @classmethod
    def vect(cls, a, v):
        return cls([a, v[0], v[1], v[2]])

    @classmethod
    def angle(cls, angle, v):
        s = np.sin(angle / 2)
        return cls([np.cos(angle / 2), s * v[0], s * v[1], s * v[2]])
