import numpy as np
from scipy.integrate import quad, simpson

f = lambda x: np.exp(-x)

exact = 1.0

print("n\tNewton-Cotes Error\tGauss Error")

for n in [2, 4, 8, 16, 32, 64]:
    x = np.linspace(0, 10, n + 1)
    y = f(x)

    nc = simpson(y, x=x)

    nodes, weights = np.polynomial.laguerre.laggauss(n)
    gauss = np.sum(weights)

    print(f"{n}\t{abs(nc-exact):.6e}\t\t{abs(gauss-exact):.6e}")