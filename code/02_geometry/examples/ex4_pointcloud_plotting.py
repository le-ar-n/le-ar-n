from random import random
from compas.geometry import Pointcloud
from compas_plotters import Plotter
from compas.utilities import i_to_green
from compas.utilities import i_to_red

# Construct a point cloud within a given box and by the number of the points in it
cloud = Pointcloud.from_bounds(10, 5, 0, 20)

# Create a list for storing the individual points
points = []

for xyz in cloud:
    n = random() # Assign a random value to the variable n
    points.append({ # Append each point in the cloud to the points-list
        'pos': xyz, # Store the properties of each point in a dictionary. Each point is represented by a circle with: 
        'radius': n, # a given radius
        'edgecolor': i_to_green(n), # edge colour
        'facecolor': i_to_red(n)}) # and face colour


plotter = Plotter(figsize=(8, 5))

# Returns a matplotlib point collection object 
plotter.draw_points(points) 
# Draw points on a 2D plot.
plotter.show()
