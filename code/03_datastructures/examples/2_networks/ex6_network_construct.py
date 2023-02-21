import os
import compas
from compas.datastructures import Network

# file path to source file
HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'lines.obj')

# construct a network from an OBJ file
network = Network.from_obj(FILE)

# print a summary of the network
print(network.summary())

# print a list of the network node
print(network.nodes())
print(list(network.nodes()))

# print a list of the network edges
print(network.edges())
print(list(network.edges()))

# print keys in a loop
for key in network.nodes():
    print('node key:', key)
for key in network.edges():
    print('edge key:', key)

