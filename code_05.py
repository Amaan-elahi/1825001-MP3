import numpy as np
import math

n = 10

x, w = np.polynomial.laguerre.laggauss(n)
I_laguerre = sum(w[i] * x[i]**2 for i in range(n))
I_laguerre_exact = 2

print("Gauss-Laguerre Result =", I_laguerre)
print("Analytical Result =", I_laguerre_exact)
print("Error =", abs(I_laguerre - I_laguerre_exact))

x, w = np.polynomial.hermite.hermgauss(n)
I_hermite = sum(w)
I_hermite_exact = math.sqrt(math.pi)

print("\nGauss-Hermite Result =", I_hermite)
print("Analytical Result =", I_hermite_exact)
print("Error =", abs(I_hermite - I_hermite_exact))