import numpy as np

x = np.array([1, 2, 3, 4])

N = len(x)

X = np.zeros(N, dtype=complex)

for k in range(N):
    for n in range(N):
        X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)

print("DFT:")
for k in range(N):
    print(f"X[{k}] =", X[k])