import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

theta0 = 1
N = 3000
T = 20
temps = np.linspace(0, T, N)

def EulerExplicite(theta0, temps):
    le = len(temps)
    h = T / (N - 1)
    theta = np.zeros(le)
    omega = np.zeros(le)

    theta[0], omega[0] = theta0, 0
    for k in range(1, le):
        theta[k] = theta[k - 1] + (h * omega[k - 1])
        omega[k] = omega[k - 1] + (h * (-np.sin(theta[k - 1])))
    return theta, omega

plt.figure()
plt.title("Courbe de phase")
plt.plot(EulerExplicite(theta0, temps)[0], EulerExplicite(theta0, temps)[1])
plt.show()
