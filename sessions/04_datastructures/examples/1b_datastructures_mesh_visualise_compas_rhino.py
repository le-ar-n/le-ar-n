import os
import compas

from compas.datastructures import Mesh
from compas_rhino.artists import MeshArtist

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

mesh = Mesh.from_obj(FILE)

artist = MeshArtist(mesh, layer="Mesh")

artist.draw_vertices()
artist.draw_edges()
artist.draw_faces()
