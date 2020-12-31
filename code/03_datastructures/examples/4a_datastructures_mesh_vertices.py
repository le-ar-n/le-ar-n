import os
import compas

from compas.datastructures import Mesh

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

mesh = Mesh.from_obj(FILE)

for key in mesh.vertices():
    print(mesh.vertex_degree(key))
    print(mesh.vertex)