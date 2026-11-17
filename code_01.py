import cmath
import math

real = float(input('Enter real component of the complex number: '))
imag = float(input('Enter imaginary component of the complex number: '))
n=3

z = complex(real, imag)

r,theta = cmath.polar(z)

roots = []

for k in range(n):
  ang = (theta + 2*k*cmath.pi)/n
  root = cmath.rect(r**(1/n), ang)
  roots.append(root)

  print(f'Root {k+1}')
  print(f'Polar Form: {r**(1/n)*complex(math.cos(ang), math.sin(ang))}')