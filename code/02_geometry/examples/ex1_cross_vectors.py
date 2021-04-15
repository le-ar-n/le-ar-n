from compas.geometry import Vector

# Create two vectors
u = Vector(1.0, 0.0, 0.0)
v = Vector(0.0, 1.0, 0.0)
a = Vector(0.0, 0.0, 0.0)

# Compute the cross product of the two vectors
uxv = u.cross(v)

# Print the cross product
print(uxv)

# Print the length of the cross product
print(uxv.length)

# TO DO
print(u.cross(v)[2] > 0)
print(v.cross(u)[2] > 0)