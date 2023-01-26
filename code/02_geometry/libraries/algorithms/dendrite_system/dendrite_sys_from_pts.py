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

Created on 27.09.2016

@author: kathrind
'''

import Rhino.Geometry as rg
import random as rnd
import math

import ghpythonlib.components as ghcomp
from libraries.useful.useful_functions import map_range


#===============================================================================
# 
#===============================================================================
class Node:
    def __init__(self, position, node_size, kill_distance):
        
        self.position = position
        self.sources = []
        self.direction = rg.Vector3d(0,0,0)
        self.distance = node_size
        self.kill_distance = kill_distance
        self.active = False
        self.energy = 1 # this should be decreased by each new branch
        self.is_end = False

#===============================================================================
# 
#===============================================================================
class Source:
    def __init__(self, position):
        self.position = position
        self.node = None


#===============================================================================
# 
#===============================================================================
class DendriteSystemPts:

    #===========================================================================
    def __init__(self, image_file=None):
        self.sources = []
        self.nodes = []
        
        self.node_size = 10
        self.kill_distance = 20
        self.node_radius = 35
        self.new_sources_per_radius = 3
        self.width = 1000
        self.height = 1000
        
        if image_file:
            #load image and overwrite width and height
            self.load_image(image_file)     
    

    #===========================================================================
    def create_sources(self, num_sources):
        sources = []
        for i in range(num_sources):
            # dart-throwing algorithm
            position = rg.Point3d(rnd.randrange(self.width), rnd.randrange(self.height), 0)
            while self.has_overlay(position, self.sources) == True:
                position = rg.Point3d(rnd.randrange(self.width), rnd.randrange(self.height), 0)
            sources.append(Source(position))
        return sources
     
    #===========================================================================
    def create_sources_around(self, position, radius, number):
        """ create sources around a given node """
        
        for i in range(number):
            rand_rad = rnd.randrange(self.node_size, radius)
            rand_vector = rg.Vector3d(rnd.uniform(-1, 1), rnd.uniform(-1, 1), 0)
            rand_vector.Unitize()
            sourcepos = position + rand_vector * rand_rad
            
            max_count = 1000
            counter = 0
            while self.has_overlay(sourcepos, self.sources) == True and counter < max_count:
                counter += 1
                rand_rad = rnd.randrange(self.node_size, radius)
                rand_vector = rg.Vector3d(rnd.uniform(-1, 1), rnd.uniform(-1, 1), 0)
                rand_vector.Unitize()
                sourcepos = position + rand_vector * rand_rad
                
            if 0 < sourcepos.X < self.width and 0 < sourcepos.Y < self.height:
                self.sources.append(Source(sourcepos))
    
    #===========================================================================
    def create_sources_around_nodes(self, nodes):
        for node in nodes:
            self.create_sources_around(node.position, self.node_radius, self.new_sources_per_radius)

    #===========================================================================
    def has_overlay(self, position, sources):
        for s in sources:
            if (s.position - position).Length <= self.node_size:
                return True
        return False
    
    #===========================================================================
    def get_active_nodes(self):
        return [node for node in self.nodes if node.active==True]
    
    #===========================================================================
    def get_end_nodes(self):
        return [node for node in self.nodes if node.is_end==True]
    
    #===========================================================================
    def create_node(self, position):
        node = Node(position, self.node_size, self.kill_distance)
        node.is_end = True
        self.nodes.append(node)
        self.create_sources_around(position, self.node_radius, self.new_sources_per_radius)
     
    #===========================================================================
    def step(self):
        '''
        0. kill sources that are too close.
        1. calculate the distance of each source to the nodes, and assign the source to the closest node.
        2. calculate for each active node the average direction where to put the next vein node.
        3. add vein node at the right place.
        '''
              
        self.kill_sources_and_assign_nodes_to_sources()      
        new_nodes = self.calc_direction_and_add_nodes() 
        node_ends = self.get_end_nodes()
        self.create_sources_around_nodes(node_ends)
        
    #===========================================================================
    def kill_sources_and_assign_nodes_to_sources(self):
        # clear all sources to calculate new ones
        for node in self.nodes:
            del node.sources[:]
            node.active = False
        
        sources = []
        for s in self.sources:
            mindistance_node, mindistance = self.calc_min_dist_to_node(s)
            if mindistance > mindistance_node.kill_distance:
                mindistance_node.active = True
                mindistance_node.sources.append(s)
                s.node = mindistance_node
                sources.append(s)
                
        del self.sources[:]
        self.sources = sources
     
    #===========================================================================
    def calc_min_dist_to_node(self, source):
        mindistance_node = self.nodes[0]
        mindistance = (mindistance_node.position - source.position).Length
        for node in self.nodes:
            dist = rg.Vector3d(node.position - source.position).Length
            if dist < mindistance:
                mindistance_node = node
                mindistance = dist
        return(mindistance_node, mindistance)
    
    #===========================================================================
    def calc_direction_and_add_nodes(self):
        new_nodes = []
        for node in self.nodes:
            if node.active == True:
                node.is_end = False
                average_vel = rg.Vector3d(0,0,0)
                for s in node.sources:
                    average_vel += rg.Vector3d(s.position - node.position)
                average_vel /= len(node.sources)
                average_vel.Unitize()
                node.direction = average_vel
                position = node.position + node.distance * node.direction
                vein = Node(position, self.node_size, self.kill_distance)
                vein.energy = node.energy * 0.98
                vein.dist = node.distance * 1.02
                vein.kill_distance = node.kill_distance * 1.02
                vein.is_end = True
                self.nodes.append(vein)
                new_nodes.append(vein)
        return new_nodes
    

