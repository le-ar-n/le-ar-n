import os
import compas

from compas.datastructures import Mesh

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

mesh = Mesh.from_obj(FILE)

mesh.update_default_edge_attributes({
    'q': 1.0,
    'f': 0.0})

for (u, v), attr in mesh.edges(data=True):
    print((u, v), attr)
