import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import root_scalar

def f(x, Y):
    y, yp = Y
    return [yp, y]

def shoot(s):
    sol = solve_ivp(f, [0, 1], [1, s], t_eval=np.linspace(0, 1, 100))
    return sol.y[1, -1]

s = root_scalar(shoot, bracket=[-2, 2]).root

x = np.linspace(0, 1, 100)
sol = solve_ivp(f, [0, 1], [1, s], t_eval=x)

print("Initial slope =", s)

plt.plot(x, sol.y[0])
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Shooting Method")
plt.grid()
plt.show()