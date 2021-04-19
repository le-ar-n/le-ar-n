import os
import compas

from compas.datastructures import Mesh

# file path to source file
HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

# construct a mesh datastrcuture from an OBJ file
mesh = Mesh.from_obj(FILE)

for key in mesh.vertices():
    print(mesh.vertex_degree(key)) # count the neighbors of a vertex
    print(mesh.vertex) # return mesh vertices

for key in mesh.vertices():
    print(mesh.vertex_coordinates(key)) # return the coordinates of a vertex
    print(mesh.vertex_normal(key)) # return the normal vector at the vertex
    print(mesh.vertex_area(key)) # compute the tributary area of a vertex

for facekey in mesh.faces():
    print(mesh.face_coordinates(facekey)) # compute the coordinates of the vertices of a face
    print(mesh.face_normal(facekey)) # compute the normal of a face
    print(mesh.face_area(facekey)) # compute the area of a face

for key in mesh.vertices():
    print(mesh.vertex_neighbors(key)) # return the neighbors of a vertex
    print(mesh.vertex_degree(key)) # count the neighbors of a vertex
    print(mesh.vertex_neighborhood(key)) # return the vertices in the neighborhood of a vertex
    print(mesh.vertex_faces(key)) # return the faces connected to a vertex

for facekey in mesh.faces():
    print(mesh.face_vertices(facekey)) # return the vertices of a face
    print(mesh.face_neighbors(facekey)) # return the neighbors of a face across its edges
    print(mesh.face_halfedges(facekey)) # the halfedges of a face

    for key in mesh.face_vertices(facekey):
        print(mesh.face_vertex_ancestor(facekey, key)) # return the n-th vertex before the specified vertex in a specific face
        print(mesh.face_vertex_descendant(facekey, key)) # return the n-th vertex after the specified vertex in a specific face
