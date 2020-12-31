import os
import compas

from compas.datastructures import Mesh

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

mesh = Mesh.from_obj(FILE)

print(mesh.default_vertex_attributes)
print(mesh.default_face_attributes)
print(mesh.default_edge_attributes)

for key, attr in mesh.vertices(data=True):
    print(key, attr)
for key, attr in mesh.faces(data=True):
    print(key, attr)
for (u, v), attr in mesh.edges(data=True):
    print((u, v), attr)
