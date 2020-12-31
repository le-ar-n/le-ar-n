from compas.geometry import cross_vectors
from compas.geometry import length_vector

u = [1.0, 0.0, 0.0]
v = [0.0, 1.0, 0.0]

uxv = cross_vectors(u, v)

print(length_vector(uxv))
