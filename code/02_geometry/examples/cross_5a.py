from compas.geometry import subtract_vectors
from compas.geometry import cross_vectors
from compas.geometry import length_vector
from compas.geometry import area_triangle

a = [0.0, 0.0, 0.0]
b = [1.0, 0.0, 0.0]
c = [0.0, 1.0, 0.0]

ab = subtract_vectors(b, a)
ac = subtract_vectors(c, a)

L = length_vector(cross_vectors(ab, ac))
A = area_triangle([a, b, c])

print(0.5 * L == A)