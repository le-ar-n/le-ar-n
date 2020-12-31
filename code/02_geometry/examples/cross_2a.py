from compas.geometry import cross_vectors
from compas.geometry import angle_vectors

u = [1.0, 0.0, 0.0]
v = [0.0, 1.0, 0.0]

print(angle_vectors(u, v))
print(angle_vectors(v, u))
