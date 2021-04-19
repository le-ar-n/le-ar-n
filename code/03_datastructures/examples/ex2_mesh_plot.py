import os
import compas

from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

# file path to source file
HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

# construct a mesh datastrcuture from an OBJ file
mesh = Mesh.from_obj(FILE)

# visualise COMPAS meshes using MeshPlotter
plotter = MeshPlotter(mesh, figsize=(12, 8))

# draw mesh vertices
plotter.draw_vertices()

# draw mesh edges
plotter.draw_edges()

# draw mesh faces
plotter.draw_faces()

# display the plot
plotter.show()