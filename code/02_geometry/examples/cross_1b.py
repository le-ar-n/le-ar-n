from compas.geometry import Vector

u = Vector(1.0, 0.0, 0.0)
v = Vector(0.0, 1.0, 0.0)

uxv = u.cross(v)

u_uxv = u.angle(uxv)
v_uxv = v.angle(uxv)

print(u_uxv)
print(v_uxv)
