import numpy as np
import matplotlib.pyplot as plt

N = 100
x = np.linspace(0, 1, N + 1)
h = 1 / N

A = np.zeros((N + 1, N + 1))
b = np.zeros(N + 1)

A[0, 0] = 1
b[0] = 1

for i in range(1, N):
    A[i, i - 1] = 1
    A[i, i] = -2 - h**2
    A[i, i + 1] = 1

A[N, N] = 1
A[N, N - 1] = -1

y = np.linalg.solve(A, b)

plt.plot(x, y, label="Numerical")
plt.plot(x, np.cosh(1 - x) / np.cosh(1), '--', label="Exact")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.legend()
plt.grid()
plt.show()