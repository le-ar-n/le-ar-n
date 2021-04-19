from random import random
from compas.geometry import Pointcloud
from compas_plotters import Plotter
from compas.utilities import i_to_green
from compas.utilities import i_to_red

# construct a point cloud within a given box and by the number of the points in it
cloud = Pointcloud.from_bounds(10, 5, 0, 20)

# create a list for storing the individual points
points = []

for xyz in cloud:
    n = random() # assign a random value to the variable n
    points.append({ # append each point in the cloud to the points-list
        'pos': xyz, # store the properties of each point in a dictionary. Each point is represented by a circle with: 
        'radius': n, # a given radius
        'edgecolor': i_to_green(n), # edge colour
        'facecolor': i_to_red(n)}) # and face colour

# visualise using Plotter
plotter = Plotter(figsize=(8, 5))

# returns a matplotlib point collection object 
plotter.draw_points(points)
 
# display the plot
plotter.show()
