from compas.geometry import cross_vectors

u = [1.0, 0.0, 0.0]
v = [0.0, 1.0, 0.0]

print(cross_vectors(u, v)[2] > 0)
print(cross_vectors(v, u)[2] > 0)
