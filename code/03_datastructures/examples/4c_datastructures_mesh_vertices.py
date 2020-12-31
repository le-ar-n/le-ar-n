import os
import compas

from compas.datastructures import Mesh

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

mesh = Mesh.from_obj(FILE)

for key in mesh.vertices():
    print(mesh.vertex_neighbors(key))
    print(mesh.vertex_degree(key))
    print(mesh.vertex_neighborhood(key))
    print(mesh.vertex_faces(key))

for fkey in mesh.faces():
    print(mesh.face_vertices(fkey))
    print(mesh.face_neighbors(fkey))
    print(mesh.face_halfedges(fkey))

    for key in mesh.face_vertices(fkey):
        print(mesh.face_vertex_ancestor(fkey, key))
        print(mesh.face_vertex_descendant(fkey, key))
