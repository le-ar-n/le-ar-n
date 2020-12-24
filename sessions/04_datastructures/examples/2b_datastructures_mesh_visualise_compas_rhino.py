import os
import compas

from compas.datastructures import Mesh
from compas_rhino.artists import MeshArtist

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

mesh = Mesh.from_obj(FILE)

artist = MeshArtist(mesh, layer="Mesh")

artist.draw_vertices(
    color={key: (255, 0, 0) for key in mesh.vertices_on_boundary()})

artist.draw_vertexlabels(
    text={key: str(mesh.vertex_degree(key)) for key in mesh.vertices()})

artist.draw_edges(
    keys=list(mesh.edges_on_boundary()),
    color=(255, 0, 0))

artist.draw_faces(
    color={key: (150, 255, 150) for key in mesh.faces() if not mesh.is_face_on_boundary(key)})
