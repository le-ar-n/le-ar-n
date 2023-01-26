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
    def __init__(self, image_file, step, black_value, max_dist_to_next_pt, num_init_walks = 10, scale_factor = 1, sources = []):
        
        if not len(sources):
            self.load_image(image_file)
            self.scale(scale_factor)
            
            # generate random points with varying density based on the image file
            self.sources = self.generate_random_points_from_image(step, black_value)
        else:
            self.sources = sources
        
        self.walks = self.init_walks(num_init_walks)
        self.dead_walks = []
        
        self.max_dist_to_next_pt = max_dist_to_next_pt
        
    def init_walks(self, num_init_walks):
        
        walks = []
        for i in range(num_init_walks):
            init_pt = self.sources.pop(rnd.randrange(0, len(self.sources)))
            walk = [init_pt] #array of pts along walk
            walks.append(walk)
        return walks
            
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
        
        if len(self.sources):
            new_walks = []
            walk_indices_to_delete = []
            for i, walk in enumerate(self.walks):
    
                current_pt = walk[-1]
                
                # now find the closest point form the sources, append it to the walk, and pop it from the sources
                min_dist, nex_pt = self.min_distance(current_pt, self.sources)
    
                
                if min_dist > self.max_dist_to_next_pt:
                    nex_pt = self.sources.pop(rnd.randrange(0, len(self.sources)))
                    new_walks.append([nex_pt])
                    walk_indices_to_delete.append(i)
                else:
                    self.sources.remove(nex_pt)
                    walk.append(nex_pt)
            
            if len(new_walks):
                for i, idx in enumerate(walk_indices_to_delete):
                    dead_walk = self.walks.pop(idx)
                    if len(dead_walk) > 1:
                        self.dead_walks.append(dead_walk)
                    self.walks.append(new_walks[i])
                        
        else:
            pass
            