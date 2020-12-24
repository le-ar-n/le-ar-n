"""Assignment:

1a Given two vectors, use the cross product to create a set of three orthonormal vectors.
1b Use the cross product to compute the area of a convex, 2D polygon.
1c Define a function for computing the cross products of two same-length arrays of vectors by
    a. Prototype in pure Python (loop over the arrays).
    b. Make Numpy equivalent without loops.
"""

# 1b. Use the cross product to compute the area of a convex, 2D polygon from the following set of points, 
# and compare your result with using the compas function area_triangle.

from compas.geometry import Vector
from compas.geometry import area_triangle

a = [0.0, 0.0, 0.0]
b = [1.0, 0.0, 0.0]
c = [0.0, 1.0, 0.0]

ab = Vector.from_start_end(a, b) #Vector1
ac = Vector.from_start_end(a, c) #Vector2

#compute the cross product using the Vector function cross cp = a.cross(b)
x = #...

#take te length of the vector
L = #...

#and divide L by 2
A1 = #...
print(A1)

#now compute the area by using the area_triangle function of compas
A2 = #...
print(A2)

#and check your result
print(A1 == A2)


