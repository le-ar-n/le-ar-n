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

# visualise COMPAS networks using NetworkPlotter
plotter = NetworkPlotter(network, figsize=(12, 8))

for key in network.leaves():
    edge = network.connected_edges(key)
    start = network.node_coordinates(edge[0][0])
    end = network.node_coordinates(edge[0][1])
    if edge[0][0] > edge[0][1]:
        u = Vector.from_start_end(end, start)
    else: 
        u = Vector.from_start_end(start, end)
    n = network.node_coordinates(key)
    print(n)
    p = Point(n[0], n[1], n[2])
    T = Translation.from_vector(u)
    p.transform(T)
    network.node_attributes(key,'xyz', [p[0], p[1], p[2]])

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