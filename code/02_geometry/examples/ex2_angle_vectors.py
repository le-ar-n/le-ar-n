import math
from compas.geometry import Vector

# create two unit vectors
u = Vector(1.0, 0.0, 0.0)
v = Vector(0.0, 1.0, 0.0)

# compute the smallest angle between this vector and another vector in radians.
print(u.angle(v))
print(v.angle(u))

# compute the smallest angle between this vector and another vector in degrees.
print(math.degrees(u.angle(v)))
print(math.degrees(u.angle(v)))