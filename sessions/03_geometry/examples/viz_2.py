from random import random
from compas.geometry import Pointcloud
from compas_plotters import Plotter
from compas.utilities import i_to_green
from compas.utilities import i_to_red

cloud = Pointcloud.from_bounds(10, 5, 0, 20)

points = []
for xyz in cloud:
    n = random()
    points.append({'pos': xyz, 'radius': n, 'edgecolor': i_to_green(n), 'facecolor': i_to_red(n)})

plotter = Plotter(figsize=(8, 5))
plotter.draw_points(points)
plotter.show()
