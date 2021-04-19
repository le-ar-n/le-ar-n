import os
import compas

from compas.datastructures import Mesh
from compas.topology import breadth_first_ordering
from compas.utilities import i_to_red
from compas_plotters import MeshPlotter

# file path to source file
HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

# construct a mesh datastrcuture from an OBJ file
mesh = Mesh.from_obj(FILE)

# set multiple attributes of multiple vertices
mesh.vertices_attributes('xyz', [0, 0, 0])

# return all vertices reachable from a chosen root vertex
bfo = breadth_first_ordering(mesh.adjacency, 0)
print(bfo)

for key, attr in mesh.vertices(data=True):
    print(key, attr)

for (u, v), attr in mesh.edges(data=True):
    print((u, v), attr)

# count the number of vertices in the mesh
n = mesh.number_of_vertices()

# visualise COMPAS meshes using MeshPlotter
plotter = MeshPlotter(mesh, figsize=(12, 8))

# draw mesh vertices
plotter.draw_vertices(
    text={key: key for key in mesh.vertices()},
    radius=0.2,
    facecolor={key: i_to_red(1 - index / n) for index, key in enumerate(bfo)})

# draw mesh edges
plotter.draw_edges()

# draw mesh faces
plotter.draw_faces()

# display the plot
plotter.show()
