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

# print node attributes etc.....
#
#
#


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