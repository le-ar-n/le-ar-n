from compas.geometry import cross_vectors
from compas.geometry import angle_vectors

u = [1.0, 0.0, 0.0]
v = [0.0, 1.0, 0.0]

uxv = cross_vectors(u, v)

u_uxv = angle_vectors(u, uxv)
v_uxv = angle_vectors(v, uxv)

print(u_uxv)
print(v_uxv)
