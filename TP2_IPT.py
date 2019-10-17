import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt

theta0 = 1
thetaPoint0 = 0.0
y0 = [theta0, thetaPoint0]
tmax = 50
n = 1000

def pendule(y, t):
    theta, omega = y
    dydt = [omega, -np.sin(theta)]
    return dydt

t = np.linspace(0, tmax, n)

"""
sol1 = spi.odeint(pendule, y0, t) # solution obtenue par odeint
sol2 = [theta0 * np.cos(temps) for temps in t]

# affichage des solutions
plt.title("Pendule")
Y1 = [x[0] for x in sol1]
plt.plot(t, sol2)
plt.plot(t, Y1)
plt.show()

# affichage de l'écart
thetas0 = np.linspace(0.01, np.pi - 0.2, 300)
Y = []
for t0 in thetas0:
    s = spi.odeint(pendule, [t0, 0.0], t)
    s1 = [x[0] for x in s]
    s2 = [t0 * np.cos(temps) for temps in t]
    M = abs(s1[0] - s2[0])
    for i in range(0, len(s1)):
        e = abs(s1[i] - s2[i])
        if e > M:
            M = e
    Y.append(np.log(M) / np.log(10))

plt.title("Ecart max")
plt.plot(thetas0, Y)
plt.show()
