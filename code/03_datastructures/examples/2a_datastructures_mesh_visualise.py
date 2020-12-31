import os
import compas

from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

mesh = Mesh.from_obj(FILE)

plotter = MeshPlotter(mesh, figsize=(16, 10))

plotter.draw_vertices(
    facecolor={key: (255, 0, 0) for key in mesh.vertices_on_boundary()},
    text={key: str(mesh.vertex_degree(key)) for key in mesh.vertices()},
    radius=0.2)

plotter.draw_edges(
    keys=list(mesh.edges_on_boundary()),
    color=(255, 0, 0))

plotter.draw_faces(
    facecolor={key: (150, 255, 150) for key in mesh.faces() if not mesh.is_face_on_boundary(key)})

plotter.show()
