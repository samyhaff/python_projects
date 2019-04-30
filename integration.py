import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

plt.figure()

f = lambda x: np.sin(x)
n = 30
a = 0
b = 2 * np.pi
X = np.linspace(a, b, n)

def rectGauche():
    I = 0
    h = (b - a) / n
    for k in range(0, n + 1):
        I += h * f(a + k * h)
        if k != n:
            plt.fill([a + k * h, a + (k + 1) * h, a + (k + 1) * h, a + k * h], [0, 0, f(a + k * h), f(a + k * h)])
    print I
    return I

def rectDroit():
    I = 0
    h = (b - a) / n
    for k in range(0, n + 1):
        I += h * f(a + (k + 1) * h)
        if k != n:
            plt.fill([a + k * h, a + (k + 1) * h, a + (k + 1) * h, a + k * h], [0, 0, f(a + (k + 1) * h), f(a + (k + 1) * h)])
    print I
    return I

def pointMilieu():
    I = 0
    h = (b - a) / n
    for k in range(0, n + 1):
        I += h * f((a + k * h + a + (k + 1) * h) / 2)
        if k != n:
            plt.fill([a + k * h, a + (k + 1) * h, a + (k + 1) * h, a + k * h], [0, 0, f((a + k * h + a + (k + 1) * h) / 2), f((a + k * h + a + (k + 1) * h) / 2)])
    print I
    return I

def trapeze():
    I = 0
    h = (b - a) / n
    for k in range(0, n + 1):
        I += h / 2 * (f(a + k * h) + f(a + (k + 1) * h))
        if k != n:
            plt.fill([a + k * h, a + (k + 1) * h, a + (k + 1) * h, a + k * h], [0, 0, f(a + (k + 1) * h), f(a + k * h)])
    print I
    return I

def simpson():
    I = 0
    h = (b - a) / n
    for k in range(0, n + 1):
        I += h / 6 * (f(a + k * h) + f(a + (k + 1) * h) + 4 * f((a + k * h + a + (k + 1) * h) / 2))
    print I
    return I

pointMilieu()
plt.plot(X, f(X), label = "f(x)", color = "black", linewidth = 2.0)
plt.xlim([a, b])
plt.ylim([-1, 1])
plt.title("intégration numérique")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
