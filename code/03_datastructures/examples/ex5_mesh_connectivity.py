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

# Return a breadth-first ordering of all vertices in an adjacency dictionary reachable from a chosen root vertex
bfo = breadth_first_ordering(mesh.adjacency, 0)
print(bfo)

n = mesh.number_of_vertices()

plotter = MeshPlotter(mesh, figsize=(12, 8))
plotter.draw_vertices(
    text={key: key for key in mesh.vertices()},
    radius=0.2,
    facecolor={key: i_to_red(1 - index / n) for index, key in enumerate(bfo)})

plotter.draw_edges()
plotter.draw_faces()
plotter.show()


# # 
# mesh.vertices_attributes('xyz', [0, 0, 0])

# bfo = breadth_first_ordering(mesh.adjacency, 0)
# print(bfo)

# for key, attr in mesh.vertices(data=True):
#     print(key, attr)

# for (u, v), attr in mesh.edges(data=True):
#     print((u, v), attr)
