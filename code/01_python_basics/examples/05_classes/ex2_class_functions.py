import random
import math

# Polygon class definition
class Polygon():
    def __init__(self, num_sides=3, radius=1.0):
        self.num_sides = num_sides
        self.radius = radius
    
    # Object method
    def get_area(self):
        a  = math.pi/self.num_sides
        hb = self.radius * math.cos(a)
        b  = self.radius * math.sin(a) * 2
        A  = (b*hb)/2
        return self.num_sides * A

# Creating an instance of the polygon class   
pol = Polygon(num_sides=6, radius=1.54)
# Printing the area
print("The polygon with {} sides and radius {} has an area of: {}".format(pol.num_sides, pol.radius, pol.get_area()))