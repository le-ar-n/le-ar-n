"""Assignment:

1a Given two vectors, use the cross product to create a set of three orthonormal vectors.
1b Use the cross product to compute the area of a convex, 2D polygon.
1c Define a function for computing the cross products of two same-length arrays of vectors by
    a. Prototype in pure Python (loop over the arrays).
    b. Make Numpy equivalent without loops.
"""

# 1c. Define a function for computing the cross products of two same-length arrays of vectors by
# a. Prototype in pure Python (loop over the arrays).
# b. Make Numpy equivalent without loops.

from compas.geometry import cross_vectors
import numpy as np

v1 = [[0.0, 1.0, 2.0],[3.0, 4.0, 5.0],[6.0, 7.0, 8.0]]
v2 = [[8.0, 7.0, 6.0],[5.0, 4.0, 3.0],[2.0, 1.0, 0.0]]

#loop over the vectors
def xproductarray(array1, array2):
    
    xproducts = []
    for i in range(len(v1)):
        x = #...
        xproducts.append(x)
    
    return xproducts

print(xproductarray(v1, v2))

#numpy equivalent (by using np.cross)
#...


