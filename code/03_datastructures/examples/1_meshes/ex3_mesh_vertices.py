import os
import compas

from compas.datastructures import Mesh

# file path to source file
HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

# construct a mesh datastructure from an OBJ file
mesh = Mesh.from_obj(FILE)

# print mesh attributes
print(mesh.default_vertex_attributes) # default vertex attributes
print(mesh.default_face_attributes) # default face attributes
print(mesh.default_edge_attributes) # default edge attributes


# print mesh vertex, face and edge attributes in a loop
for key, attr in mesh.vertices(data=True):
    print(key, attr)
for key, attr in mesh.faces(data=True):
    print(key, attr)
for (u, v), attr in mesh.edges(data=True):
    print((u, v), attr)

# update default edge attributes
mesh.update_default_edge_attributes({
    'q': 1.0,
    'f': 0.0})

# print edge attributes in a loop
for (u, v), attr in mesh.edges(data=True):
    print((u, v), attr)

# print vertex attributes
print(mesh.vertex_attribute(0, 'x')) # mesh vertex attribute
print(mesh.vertex_attributes(0, 'xyz')) # mesh vertex attributes
print(mesh.vertices_attribute('x')) # mesh vertices attribute
print(mesh.vertices_attributes('xyz')) # mesh vertices attributes

# Selection
mesh.vertices_where({'x': 1.0, 'y': (0.0, 10.0)}) # get vertices for which a certain condition or set of conditions is true

a = mesh.vertices_where({'x': 1})
b = mesh.vertices_where({'x': (5, 10)})
print(list(a)+list(b))
