import numpy as np
import matplotlib.pyplot as plt

max_iterations = 120
density = 5000

X = np.linspace(-2, 1.5, density)
Y = np.linspace(-1, 1, density)
Xlen = len(X)
Ylen = len(Y)
img = np.empty((Xlen, Ylen))

plt.figure(figsize = (10, 6))
plt.axis('off')

def mandelbrot(c, max_iterations):
    z = complex(0, 0)
    for i in range(max_iterations):
        z = (z*z) + c
        if abs(z) > 4:
            break
    return i

for ix in range(Xlen):
    for iy in range(Ylen):
        cx = X[ix]
        cy = Y[iy]
        c = complex(cx, cy)
        img[ix, iy] = mandelbrot(c, max_iterations)

plt.imshow(img.T, interpolation= "nearest")
plt.show()
