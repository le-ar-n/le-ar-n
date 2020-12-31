from compas.geometry import Vector
from compas.geometry import area_triangle

a = [0.0, 0.0, 0.0]
b = [1.0, 0.0, 0.0]
c = [0.0, 1.0, 0.0]

ab = Vector.from_start_end(a, b)
ac = Vector.from_start_end(a, c)

L = ab.cross(ac).length
A = area_triangle([a, b, c])

print(0.5 * L == A)