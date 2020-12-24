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

bfo = breadth_first_ordering(mesh.adjacency, 0)

print(bfo)

n = mesh.number_of_vertices()

plotter = MeshPlotter(mesh, figsize=(16, 10))
plotter.draw_vertices(
    text={key: key for key in mesh.vertices()},
    radius=0.2,
    facecolor={key: i_to_red(1 - index / n) for index, key in enumerate(bfo)})

plotter.draw_edges()
plotter.draw_faces()
plotter.show()