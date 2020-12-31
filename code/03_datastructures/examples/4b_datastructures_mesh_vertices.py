import os
import compas

from compas.datastructures import Mesh

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

mesh = Mesh.from_obj(FILE)

for key in mesh.vertices():
    print(mesh.vertex_coordinates(key))
    print(mesh.vertex_normal(key))
    print(mesh.vertex_area(key))

for fkey in mesh.faces():
    print(mesh.face_coordinates(fkey))
    print(mesh.face_normal(fkey))
    print(mesh.face_area(fkey))
