from random import random
from compas.geometry import pointcloud_xy
from compas_plotters import Plotter
from compas.utilities import i_to_green
from compas.utilities import i_to_red

cloud = pointcloud_xy(20, (0, 10), (0, 5))

points = []
for xyz in cloud:
    n = #...
    points.append({'pos': xyz, 'radius': ..., 'edgecolor': ..., 'facecolor': ...})

plotter = Plotter(figsize=(8, 5))
plotter.draw_points(points)
plotter.show()
