import cmath
import math

z = 3+4j

#Translation
transalation = 1+2j
translated = z + transalation

#Scaling
scale = 2
scaled = 2*z

#Rotation
theta = math.radians(90)
rot = complex(math.cos(theta), math.sin(theta))
rotated = z * rot

#Reflection by X-axis
reflected_x = z.conjugate()

#Reflection by Y-axis
reflected_y = -z.conjugate()

print('Original:', z)
print("Translation:", translated)
print("Scaling:", scaled)
print("Rotation:", rotated)
print("Reflection about x-axis:", reflected_x)
print("Reflection about y-axis:", reflected_y)