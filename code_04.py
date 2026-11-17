import numpy as np
from numpy.polynomial import legendre

def f(x):
    return x**2

a = -1
b = 1

n = 3

x, w = legendre.leggauss(n)

I = 0

for i in range(n):
    I += w[i] * f(x[i])

print("Definite Integral =", I)

coefficients = []

for k in range(n):
    integral = 0

    for i in range(n):
        Pk = legendre.Legendre.basis(k)(x[i])
        integral += w[i] * f(x[i]) * Pk

    ck = ((2*k + 1) / 2) * integral
    coefficients.append(ck)

print("\nLegendre Coefficients:")

for k, c in enumerate(coefficients):
    print(f"c{k} =", c)