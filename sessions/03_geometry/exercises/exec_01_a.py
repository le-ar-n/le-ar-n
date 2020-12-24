"""Assignment:

1a Given two vectors, use the cross product to create a set of three orthonormal vectors.
1b Use the cross product to compute the area of a convex, 2D polygon.
1c Define a function for computing the cross products of two same-length arrays of vectors by
    a. Prototype in pure Python (loop over the arrays).
    b. Make Numpy equivalent without loops.
"""

# 1a. Given two vectors, use the cross product to create a set of three orthonormal vectors.

from compas.geometry import cross_vectors
from compas.geometry import angle_vectors
import math as m

v1 = [1,2,3]
v2 = [4,5,6]

# replace #... and fill in there
x1 = #...
x2 = #...
x3 = #...

print(x1)
print(x2)
print(x3)

print(m.degrees(angle_vectors(x1, x2)))
print(m.degrees(angle_vectors(x1, x3)))
print(m.degrees(angle_vectors(x2, x3)))     