import os
import compas
from compas.datastructures import Network
from compas_plotters import NetworkPlotter

# Create a file path to lines.obj
HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'lines.obj')

# Construct a network from the data contained in an OBJ file
network = Network.from_obj(FILE)

# Print a summary of the graph.
print(network.summary())

# Visualize network using MeshPlotter 
plotter = NetworkPlotter(network, figsize=(12, 8))
plotter.draw_nodes(
    text='key',
    facecolor={key: '#ff0000' for key in network.leaves()},
    radius=0.15
)
plotter.draw_edges()
plotter.show()