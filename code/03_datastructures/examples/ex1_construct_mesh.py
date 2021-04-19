import os
import compas

from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

mesh = Mesh.from_obj(FILE)

print(mesh.summary())

# Print a list of the mesh vertices
print(mesh.vertices())
print(list(mesh.vertices()))

# Print a list of the mesh faces
print(mesh.faces())
print(list(mesh.faces()))

# Print a list of the mesh edges
print(mesh.edges())
print(list(mesh.edges()))

# Print keys
for key in mesh.vertices():
    print('vertex key:', key)
for key in mesh.faces():
    print('face key:',key)
for key in mesh.edges():
    print('edge key:',key)

plotter = MeshPlotter(mesh, figsize=(12, 8))

plotter.draw_vertices()
plotter.draw_edges()
plotter.draw_faces()

plotter.show()