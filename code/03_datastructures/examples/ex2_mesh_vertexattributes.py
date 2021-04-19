import os
import compas

from compas.datastructures import Mesh

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

mesh = Mesh.from_obj(FILE)


print(mesh.default_vertex_attributes) # Default vertex attributes.
print(mesh.default_face_attributes) # Default face attributes.
print(mesh.default_edge_attributes) # Default edge attributes.

# # Print mesh vertex, face and edge attributes for each vertex, face and edge of the mesh object
# for key, attr in mesh.vertices(data=True):
#     print(key, attr)
# for key, attr in mesh.faces(data=True):
#     print(key, attr)
# for (u, v), attr in mesh.edges(data=True):
#     print((u, v), attr)


# Update the default edge attributes
mesh.update_default_edge_attributes({
    'q': 1.0,
    'f': 0.0})

for (u, v), attr in mesh.edges(data=True):
    # print((u, v), attr) # edge attributes

    # print(mesh.vertex_attribute(0, 'x')) # mesh vertex attribute

    # print(mesh.vertex_attributes(0, 'xyz')) # mesh vertex attributes

    # print(mesh.vertices_attribute('x')) # mesh vertices attribute

    print(mesh.vertices_attributes('xyz')) # mesh vertices attributes
