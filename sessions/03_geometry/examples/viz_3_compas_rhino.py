from random import random
from compas.geometry import Pointcloud
from compas.geometry import Point, Circle, Plane
from compas.utilities import i_to_green
from compas.utilities import i_to_red
from compas_rhino.artists import PointArtist, CircleArtist

cloud = Pointcloud.from_bounds(10, 5, 0, 50)

for point in cloud:
    n = random()
    
    PointArtist(point, color=i_to_red(n), layer="points").draw()
    
    
    radius = n
    plane = Plane([0, 0, 0], [0, 0, 1])
    circle = Circle(plane, radius)
    circle.center = point

    CircleArtist(circle, color=i_to_red(n), layer="circles").draw()