"""Nested iterative statement"""

x_size = 3
y_size = 4
z_size = 2

point_list = []

for x in range(x_size):
    for y in range(y_size):
        for z in range(z_size):
            print("Point3D:", (x, y, z))
            point_list.append((x,y,z))
else:
    print("All points are generated")

print(point_list)