import numpy as np
import matplotlib.pyplot as plt

N = 256
x = np.linspace(-5, 5, N)

f = np.exp(-x**2)

F = np.fft.fft(f)
f_inverse = np.fft.ifft(F)

plt.plot(x, f, label="Original")
plt.plot(x, np.real(f_inverse), '--', label="Inverse FT")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()