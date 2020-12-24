import os
import compas

from compas.datastructures import Mesh

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

mesh = Mesh.from_obj(FILE)

print(mesh.vertex_attribute(0, 'x'))

print(mesh.vertex_attributes(0, 'xyz'))

print(mesh.vertices_attribute('x'))

print(mesh.vertices_attributes('xyz'))
