import os
import compas

from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

mesh = Mesh.from_obj(FILE)

plotter = MeshPlotter(mesh, figsize=(16, 10))

plotter.draw_vertices()
plotter.draw_edges()
plotter.draw_faces()

plotter.show()
