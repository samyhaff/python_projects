"""
Features:
racines #renvoie liste des racines
factoriser #renvoie string
addition #renvoie polynome 1 COMPLETED
multiplication #renvoie polynome 2 COMPLETED
pgcd #renvoie polynome 5
taylor #renvoie un string
dérivées #renvoie un polynome 3 COMPLETED
print #affiche un string 0 COMPLETED
racines complexes
"""

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

    def derivative(self):
        newcoefficients=[i*c for (i,c) in enumerate(self.coefficients)]
        del newcoefficients[0]
        return Polynome(newcoefficients)

    def pgcd(self):
        pass

    def division(self, A, B):
        delta=len(A)
        C=[0]*+B
        [3,2,4,5,1],[0,0,1/3,4/3,1]

        len(B)
        A[-1]
        B[-1]

        return (Q, R)

if __name__ == "__main__":
    coeffs1 = [1,1]
    coeffs2 = [-1,1]
    polynome1 = Polynome(coeffs1)
    polynome2 = Polynome(coeffs2)
    sum = polynome1 + polynome2
    mul = polynome1 * polynome2
    print(sum)
    print(mul)
