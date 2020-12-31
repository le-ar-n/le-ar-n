from compas.geometry import Vector

u = Vector(1.0, 0.0, 0.0)
v = Vector(0.0, 1.0, 0.0)

print(u.cross(v)[2] > 0)
print(v.cross(u)[2] > 0)
