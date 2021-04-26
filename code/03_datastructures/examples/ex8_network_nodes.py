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

# print a summary of the network
print(network.summary())

# print node attributes
for key, attr in network.nodes(data=True):
    print(key, attr)

# print edge attributes
for (u, v), attr in network.edges(data=True):
    print((u, v), attr)

# print node attributes
print(network.node_attribute(0, 'x')) # node attribute
print(network.node_attributes(0, 'xyz')) # node attributes
print(network.nodes_attribute('x')) # nodes attribute
print(network.nodes_attributes('xyz')) # nodes attributes

# Selection
print(network.nodes_where({'x': (0.0, 10.0)})) # get nodes for which a certain condition or set of conditions is true

for node in network.nodes_where({'x': (0.0, 10.0)}):
    print(node)

# visualise COMPAS networks using NetworkPlotter
plotter = NetworkPlotter(network, figsize=(12, 8))

# draw network nodes
plotter.draw_nodes(
    text='key',
    radius=0.15
)
# draw network edges
plotter.draw_edges()

# display the plot
plotter.show()