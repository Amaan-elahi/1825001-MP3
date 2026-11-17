import numpy as np
import matplotlib.pyplot as plt

N = 50
T = np.zeros((N, N))

T[0, :] = 100
T[:, 0] = 0
T[:, -1] = 0
T[-1, :] = 0

for k in range(10000):
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            T[i, j] = 0.25 * (T[i+1, j] + T[i-1, j] + T[i, j+1] + T[i, j-1])

plt.imshow(T, origin='lower', extent=[0, 1, 0, 1])
plt.colorbar(label="Temperature")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Solution of Laplace Equation")
plt.show()