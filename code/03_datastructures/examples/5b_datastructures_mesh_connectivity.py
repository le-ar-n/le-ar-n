import os
import compas

from compas.datastructures import Mesh
from compas.topology import breadth_first_ordering
from compas.utilities import i_to_red
from compas_plotters import MeshPlotter

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

mesh = Mesh.from_obj(FILE)

mesh.vertices_attributes('xyz', [0, 0, 0])

bfo = breadth_first_ordering(mesh.adjacency, 0)

print(bfo)

for key, attr in mesh.vertices(data=True):
    print(key, attr)

for (u, v), attr in mesh.edges(data=True):
    print((u, v), attr)
