import os
import compas

from compas.datastructures import Mesh

# file path to source file
HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

# construct a mesh datastructure from an OBJ file
mesh = Mesh.from_obj(FILE)

# print a summary of the mesh
print(mesh.summary())

# print a list of the mesh vertices
print(mesh.vertices())
print(list(mesh.vertices()))

# print a list of the mesh faces
print(mesh.faces())
print(list(mesh.faces()))

# print a list of the mesh edges
print(mesh.edges())
print(list(mesh.edges()))

# print keys in a loop
for key in mesh.vertices():
    print('vertex key:', key)
for key in mesh.faces():
    print('face key:',key)
for key in mesh.edges():
    print('edge key:',key)
