import matplotlib.pyplot as plt
import numpy as np
import math
import random

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.xlim(X.min()*1.1, X.max()*1.1)
plt.ylim(C.min()*1.1, C.max()*1.1)

plt.figure(figsize = (10,6), dpi = 80)

plt.plot(X, C, color=(0,0,0), linewidth=2.5, linestyle="-", label="cosinus")
plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sinus")

plt.title("cos et sin")
plt.legend(loc='upper left', frameon=False)
plt.xlabel("x")
plt.ylabel("y")

plt.show()
