from compas.geometry import Vector

# create two unit vectors
u = Vector(1.0, 0.0, 0.0)
v = Vector(0.0, 1.0, 0.0)

# compute the cross product of the two vectors
uxv = u.cross(v)

# print the cross product
print(uxv)

# print the length of the cross product
print(uxv.length)

# print if the z-component of the cross product is positive (if the cross product shows in the positive z-direction) 
print(u.cross(v)[2] > 0)
print(v.cross(u)[2] > 0)