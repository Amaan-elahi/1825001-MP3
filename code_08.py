import numpy as np
import matplotlib.pyplot as plt

N = 256
x = np.linspace(-5, 5, N)

f = np.exp(-x**2)

F = np.fft.fft(f)
freq = np.fft.fftfreq(N, x[1] - x[0])

F = np.fft.fftshift(F)
freq = np.fft.fftshift(freq)

plt.plot(freq, np.abs(F))
plt.xlabel("Frequency")
plt.ylabel("|F(k)|")
plt.title("FFT of exp(-x²)")
plt.grid()
plt.show()