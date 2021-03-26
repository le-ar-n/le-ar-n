from random import random
from compas.geometry import Pointcloud
from compas.geometry import Point, Circle, Plane
from compas_plotters import Plotter
from compas.utilities import i_to_green
from compas.utilities import i_to_red

cloud = Pointcloud.from_bounds(10, 5, 0, 20)
points = []
cirlces = []

for xyz in cloud:
    print(xyz)
    n = random()

    points.append(xyz)
    
    radius = n
    plane = Plane(xyz, [0,0,1])
    circle = Circle(plane, radius)
        # 'edgecolor': i_to_green(n), 
        # 'facecolor': i_to_red(n)})

plotter = Plotter(figsize=(8, 5))
plotter.draw_lines(points)
plotter.show()
