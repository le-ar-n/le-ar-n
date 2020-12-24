from compas.geometry import Vector

u = Vector(1.0, 0.0, 0.0)
v = Vector(0.0, 1.0, 0.0)

uxv = u.cross(v)

print(uxv)
