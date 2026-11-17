import numpy as np
import matplotlib.pyplot as plt

L = 10
T0 = 100
TL = 50

x = np.linspace(0, L, 100)
T = T0 + (TL - T0) * x / L

plt.plot(x, T)
plt.xlabel("Position x")
plt.ylabel("Temperature T")
plt.title("Equilibrium Temperature Distribution")
plt.grid()
plt.show()