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
from libraries.useful import clamp, map_range
from libraries.geometry.vector import get_vector_sum
from libraries.useful.color import convert_rgb_to_grey

#===============================================================================
NODE_SIZE = 0.8
NODE_SIZE_MIN = 0.8
NODE_SIZE_MAX = 3.2
 
KILL_DISTANCE_MIN = 3
KILL_DISTANCE_MAX = 20
KILL_DISTANCE = KILL_DISTANCE_MIN
RADIUS_MIN = KILL_DISTANCE_MIN * 2
RADIUS_MAX = KILL_DISTANCE_MAX * 2
RADIUS = RADIUS_MIN
STEP_SIZE = 2
STEP_SIZE_MIN = 3
STEP_SIZE_MAX = 10
 
SMALL_VALUE = 0.00001


#===============================================================================
class Node:
    def __init__(self, position):
        self.position = position
        self.sources = []
        self.direction = rg.Vector3d(0,0,0)
        self.kill_distance = KILL_DISTANCE # distance of within sources are "killed"
        self.node_size = NODE_SIZE # the size of the node
        self.step_size = STEP_SIZE
        self.radius = RADIUS # radius of affecting sources
        self.children = 0 # amount of children
        self.parent = None # the parent Node
        self.active = True # if sources cannot be assigned to the node, it is not active anymore
         
#===============================================================================
class DendriteSystemImg:
    
    #===========================================================================
    def __init__(self, image_file, step, black_value, num_init_nodes, thresh_nodes):
        self.nodes = []
        self.load_image(image_file) 
        self.sources = self.generate_random_sources_from_image(step, black_value)
        self.generate_init_nodes_from_image(num_init_nodes, thresh_nodes)

    #===========================================================================
    def load_image(self, image_file):
        self.cmesh = ghcomp.ImportImage(image_file)
        bb = self.cmesh.GetBoundingBox(rg.Plane.WorldXY)
        self.width = bb.Max.X
        self.height = bb.Max.Y
        self.point_cloud = rg.PointCloud(self.cmesh.Vertices.ToPoint3dArray())
    
    #===========================================================================   
    def get_color_grey(self, x, y):     
        point = rg.Point3d(x, y, 0)
        color_rgb = self.cmesh.VertexColors[self.point_cloud.ClosestPoint(point)]
        grey = convert_rgb_to_grey(color_rgb.R, color_rgb.G, color_rgb.B)   
        grey = clamp(grey, 0, 255)
        return grey
        
    #===========================================================================
    def generate_random_sources_from_image(self, step, black_value):
        '''Read pixel values from an image and according to the grey value in every pixel, create random 
        points. The size is adjustable with 'step' and the amount of points in black with 'black_value'.'''

        random_points = []

        for x in range(int(self.width / float(step))):
            for y in range(int(self.height / float(step))): 
                #amount = int(map_range(pix[x, y], 0, 255, black_value, 0))
                grey = self.get_color_grey(x*step, y*step)
                amount = int(map_range(grey, 0, 255, black_value, 0))
                for i in range(amount):
                    rndx = x*step + rnd.uniform(-1, 1)*step
                    rndy = y*step + rnd.uniform(-1, 1)*step
                    random_points.append(rg.Point3d(rndx, rndy, 0))
        
        return random_points
    
    #===========================================================================
    def generate_init_nodes_from_image(self, num_init_nodes, thresh_nodes):  
        
        # dart-throwing algorithm
        for i in range(num_init_nodes * 10):  
            tx = math.floor(rnd.random() * self.width)
            ty = math.floor(rnd.random() * self.height)
            
            grey = self.get_color_grey(tx, ty)
            if grey < thresh_nodes:
                position = rg.Point3d(tx, ty, 0)
                self.create_node(position)
                
            if len(self.nodes) == num_init_nodes:
                break
    
    #===========================================================================
    def create_node(self, position):
        node = Node(position)
        self.nodes.append(node)
    
    #===========================================================================
    def map_value_from_position(self,position):
        value = self.get_color_grey(position.X, position.Y)
        kill_distance = map_range(value, 0, 255, KILL_DISTANCE_MIN, KILL_DISTANCE_MAX)
        node_size = map_range(value, 0, 255, NODE_SIZE_MIN, NODE_SIZE_MAX)
        radius = map_range(value, 0, 255, RADIUS_MIN, RADIUS_MAX)
        step_size = map_range(value, 0, 255, STEP_SIZE_MIN, STEP_SIZE_MAX)
        return kill_distance, node_size, radius, step_size
    

    #===========================================================================
    def min_distance(self, s, others):
        distances = [s.DistanceTo(o) for o in others]
        min_distance = min(distances)
        other = others[distances.index(min_distance)]
        return min_distance, other
    
    #===========================================================================
    def kill_sources_and_get_sources_within_radius(self, node):
    
        # compute squared distances
        distances = [source.DistanceTo(node.position)**2 for source in self.sources]
        dist_idx_sorted = [i[0] for i in sorted(enumerate(distances), key=lambda x:x[1])]
        
        sources_within_radius = []
        sources_to_kill = []
        squared_radius = node.radius * node.radius
        squared_killdist = node.kill_distance * node.kill_distance
        
        for i, d in enumerate(dist_idx_sorted):
            if distances[d] <= squared_killdist:
                sources_to_kill.append(d)
            elif squared_killdist < distances[d] < squared_radius:
                sources_within_radius.append(self.sources[d])
            else:
                break


        new_sources = [i for j, i in enumerate(self.sources) if j not in sources_to_kill]
        self.sources = new_sources
        
        return sources_within_radius
     
    #===========================================================================
    def get_closest_node_to_source(self, active_nodes, source):
        # array of active node positions
        # source = rg.Point3d

        #distances = ((nodes_npa-[x,y])**2).sum(axis=1)  # compute squared distances
        distances = [node.position.DistanceTo(source)**2 for node in active_nodes] # compute squared distances
        dist_idx_sorted = [i[0] for i in sorted(enumerate(distances), key=lambda x:x[1])] # indirect sort
        return active_nodes[dist_idx_sorted[0]] # return node closest to source
    
    #===========================================================================  
    def step(self):
         
        active_nodes = [n for n in self.nodes if n.active == True]
        max_children = max([n.children for n in self.nodes])
        
        
        # assign sources to each node 
        for n in active_nodes:
            n.sources = [] # delete everything to reassign
            if max_children > 0:
                # adjust the node size according to the amount of their children
                n.node_size = map_range(n.children, 0, max_children, NODE_SIZE_MIN, NODE_SIZE_MAX)    
             
            # 1. kill the sources which are too close and assign sources to the node
            sources = self.kill_sources_and_get_sources_within_radius(n)
             
            # now we have to check whether one of this sources belongs to another node
            for source in sources:
                closest_node = self.get_closest_node_to_source(active_nodes, source)
                if n.position.DistanceTo(closest_node.position) < SMALL_VALUE: # n is the closest node to s
                    n.sources.append(source)
             
            # set n.active False if no sources can be assigned
            if not len(n.sources):
                n.active = False
             
        # calculate for each active node the average direction where to put the next node
        active_nodes = [n for n in self.nodes if n.active == True]
        
        for n in active_nodes:
            
            vec_list = [rg.Vector3d(source - n.position) for source in n.sources]
            sum_vec = rg.Vector3d(get_vector_sum(vec_list))
            n.direction = (sum_vec/len(n.sources))
            n.direction.Unitize()
            
            new_position = n.position + n.direction * n.step_size
             
            if not (0 <= new_position.X < self.width and 0 <= new_position.Y < self.height):
                continue
            
            # add new node at the right place
            new_node = Node(new_position)
            kill_distance, node_size, radius, step_size = self.map_value_from_position(new_position)
            new_node.kill_distance = kill_distance
            #new_node.node_size = node_size
            new_node.radius = radius
            new_node.step_size = step_size
            new_node.parent = n
            
            self.add_child_to_all_parents(n)
            self.nodes.append(new_node)
         
        print "len(self.nodes)", len(self.nodes)
         
    #===========================================================================
    def add_child_to_all_parents(self, node):
         
        def add_child_to_parent(node):
            if node.parent:
                node.parent.children += 1
                return True
            else:
                return False
             
        while add_child_to_parent(node):
            node = node.parent