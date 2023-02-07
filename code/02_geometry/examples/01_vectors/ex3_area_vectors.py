from compas.geometry import Vector
from compas.geometry import area_triangle

# construct three points as lists containing three numbers for the X, Y and Z coordinate values of the point
a = [0.0, 0.0, 0.0]
b = [1.0, 0.0, 0.0]
c = [0.0, 1.0, 0.0]

# construct two vectors from start and end points
ab = Vector.from_start_end(a, b)
ac = Vector.from_start_end(a, c)

# the length of the cross product
L = ab.cross(ac).length

# compute the area of a triangle defined by three points
A = area_triangle([a, b, c])

# print if half the length of the cross product equals the area of the triangle
print(0.5 * L == A)

