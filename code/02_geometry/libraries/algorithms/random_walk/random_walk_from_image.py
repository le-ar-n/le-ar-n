'''
. . . . . . . . . . . . . . . . . . . . . 
.                                       .
.    <<      ><      ><       >< <<     .
.    < ><   ><<     ><<<    ><    ><<   .
.    << >< > ><    ><  ><     ><        .  
.    <<  ><  ><   ><<<<<><      ><      .
.    <<      >< ><<     ><< ><    ><<   .
.    <<      ><><<       ><<  >< <<     .
.                                       .
.             DFAB 2016/17              .
. . . . . . . . . . . . . . . . . . . . . 

Created on 03.10.2016

@author: kathrind

'''

import math
import random as rnd
import ghpythonlib.components as ghcomp
import Rhino.Geometry as rg
from libraries.useful import clamp, map_range
from libraries.geometry.vector import get_vector_sum
from libraries.useful.color import convert_rgb_to_grey


#===============================================================================
class RandomWalkImg:

    #===========================================================================
    def __init__(self, image_file, step, black_value, max_dist_to_next_pt, scale_factor = 1):
        
        self.load_image(image_file)
        self.scale(scale_factor)
        
        # generate random points with varying density based on the image file
        self.sources = self.generate_random_points_from_image(step, black_value)
        
        self.walk_current_pt = self.sources.pop()
        self.walk = [self.walk_current_pt] #array of pts along walk
        self.dead_walks = []
        
        self.max_dist_to_next_pt = max_dist_to_next_pt
        
    #===========================================================================
    def load_image(self, image_file):
        self.cmesh = ghcomp.ImportImage(image_file)
        bb = self.cmesh.GetBoundingBox(rg.Plane.WorldXY)
        self.width = bb.Max.X
        self.height = bb.Max.Y
        self.point_cloud = rg.PointCloud(self.cmesh.Vertices.ToPoint3dArray())

    #===========================================================================
    def scale(self, factor):
        S = rg.Transform.Scale(rg.Plane.WorldXY, factor, factor, factor)
        self.cmesh.Transform(S)
        self.point_cloud.Transform(S)
        self.width *= factor
        self.height *= factor
    
    #===========================================================================   
    def get_grey_value(self, x, y):     
        point = rg.Point3d(x, y, 0)
        color_rgb = self.cmesh.VertexColors[self.point_cloud.ClosestPoint(point)]
        grey = convert_rgb_to_grey(color_rgb.R, color_rgb.G, color_rgb.B)   
        grey = clamp(grey, 0, 255)
        return grey
    
    #===========================================================================
    def generate_random_points_from_image(self, step, black_value):
        '''Read pixel values from an image and according to the grey value in every pixel, create random 
        points. The size is adjustable with 'step' and the amount of points in black with 'black_value'.'''

        random_points = []

        for x in range(int(self.width / float(step))):
            for y in range(int(self.height / float(step))): 
                grey = self.get_grey_value(x*step, y*step)
                amount = int(map_range(grey, 0, 255, black_value, 0))
                for i in range(amount):
                    rndx = x*step + rnd.uniform(-1, 1)*step
                    rndy = y*step + rnd.uniform(-1, 1)*step
                    random_points.append(rg.Point3d(rndx, rndy, 0))
        
        return random_points
     
    #===========================================================================
    def min_distance(self, s, others):
        distances = [s.DistanceTo(o) for o in others]
        min_distance = min(distances)
        other = others[distances.index(min_distance)]
        return min_distance, other

    #===========================================================================
    def step(self):
        
        # now find the closest point form the sources, append it to the walk, and pop it from the sources
        min_dist, other = self.min_distance(self.walk_current_pt, self.sources)
        
        print min_dist
        
        self.sources.remove(other)
        self.walk.append(other)
        self.walk_current_pt = other
        
    #===========================================================================
    def step_with_max_dist(self):
        
        # now find the closest point form the sources, append it to the walk, and pop it from the sources
        min_dist, other = self.min_distance(self.walk_current_pt, self.sources)
        
        self.sources.remove(other)
        self.walk_current_pt = other
        
        if min_dist > self.max_dist_to_next_pt:
            if len(self.walk) > 1:
                self.dead_walks.append(self.walk)
            self.walk = [self.walk_current_pt]
        else:
            self.walk.append(other)
            