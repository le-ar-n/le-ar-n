from compas.geometry import Pointcloud
from compas_plotters import Plotter

cloud = Pointcloud.from_bounds(10, 5, 0, 20)

points = []
for xyz in cloud:
    points.append({'pos': xyz, 'radius': 0.1})

plotter = Plotter(figsize=(8, 5))
plotter.draw_points(points)
plotter.show()
