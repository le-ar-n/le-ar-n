import os
import compas
from compas.datastructures import Network
from compas.geometry import Vector, Translation, Point
from compas_plotters import NetworkPlotter

# file path to source file
HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'lines.obj')

# construct a network from an OBJ file
network = Network.from_obj(FILE)

# example: move the leaves (=nodes with only one neighbor) of the network for 3 units along the edge vector to the outside
for key in network.leaves(): # loop through the leaves of the network
    neighbor = network.neighbors(key)[0] # get the neighbor from the leaf

    start = network.node_coordinates(neighbor) # get the coordinates of the start point
    end = network.node_coordinates(key) # get the coordinates of the end point

    vector = Vector.from_start_end(start, end) # create vector from start and end point
    vector.unitize() # unitize the vector
    vector *= 3 # multiply by 3

    T = Translation.from_vector(vector) # create a translation from the vector

    new_point = Point(*tuple(end)) # create a new point from the coordinates of the end point
    new_point.transform(T) # translate the new point with the translation T

    network.node_attributes(key, 'xyz', [*tuple(new_point)]) # set the new node coordinates with the getter/setter method node_attributes

# visualise COMPAS networks using NetworkPlotter
plotter = NetworkPlotter(network, figsize=(12, 8))

# draw network nodes
plotter.draw_nodes(
    text='key',
    facecolor={key: '#ff0000' for key in network.leaves()},
    radius=0.15
)
# draw network edges
plotter.draw_edges()

# display the plot
plotter.show()