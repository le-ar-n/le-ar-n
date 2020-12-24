import os
import compas
from compas.datastructures import Network

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'lines.obj')

network = Network.from_obj(FILE)

print(network.summary())
