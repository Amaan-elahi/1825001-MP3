import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)

X, Y = np.meshgrid(x, y)

z = X+1j*Y
w = z**2

fig, ax = plt.subplots(1, 2)

ax[0].scatter(z.real, z.imag)
ax[0].set_title("z-plane")
ax[0].set_xlabel("Real")
ax[0].set_ylabel("Imaginary")
ax[0].grid()

ax[1].scatter(w.real, w.imag)
ax[1].set_title("w-plane")
ax[1].set_xlabel("Real")
ax[1].set_ylabel("Imaginary")
ax[1].grid()

plt.show()