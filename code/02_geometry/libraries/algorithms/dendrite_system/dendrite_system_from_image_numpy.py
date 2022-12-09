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

@author: rustr
'''

import random as rnd
import math
import numpy as np
from PIL import Image

from libraries.useful import clamp, map_range
from libraries.useful.color import convert_rgb_to_grey


#===============================================================================
# Globals

NODE_SIZE = 0.8
NODE_SIZE_MIN = 0.8
NODE_SIZE_MAX = 3.2
 
KILL_DISTANCE_MIN = 2
KILL_DISTANCE_MAX = 10
KILL_DISTANCE = KILL_DISTANCE_MIN
RADIUS_MIN = KILL_DISTANCE_MIN * 2
RADIUS_MAX = KILL_DISTANCE_MAX * 2
RADIUS = RADIUS_MIN
STEP_SIZE = 2
STEP_SIZE_MIN = 3
STEP_SIZE_MAX = 10
 
SMALL_VALUE = 0.00001
#===============================================================================

 
#===============================================================================
class Node:
    def __init__(self, position):
        self.position = position
        self.sources = []
        self.direction = np.array([0,0,0])
        self.kill_distance = KILL_DISTANCE # distance of within sources are "killed"
        self.node_size = NODE_SIZE # the size of the node
        self.step_size = STEP_SIZE
        self.radius = RADIUS # radius of affecting sources
        self.num_children = 0 # amount of children
        self.parent = None # the parent Node
        self.children = []
        self.active = True # if sources cannot be assigned to the node, it is not active anymore   
#===============================================================================


#===============================================================================
class DendriteSystemFromImage:
    
    #===========================================================================
    def __init__(self, image_file, step, black_value, num_init_nodes, thresh_nodes):
        self.nodes = []
        self.new_nodes = []
        self.active_nodes = []
        self.load_image(image_file) 
        self.sources = self.generate_random_sources_from_image(step, black_value)
        self.generate_init_nodes_from_image(num_init_nodes, thresh_nodes)

    #===========================================================================
    def load_image(self, image_file):
        from PIL import Image
        image = Image.open(image_file).convert("L")
        width, height = image.size
        self.width = width
        self.height = height
        self.pix = image.load()
            
    #===========================================================================   
    def get_color_grey(self, x, y): 
        tx = int(self.width - math.floor(x)) % self.width # PIL is flipped
        ty = int(self.height-math.floor(y)) % self.height
        grey = self.pix[tx, ty]
        return grey
        
    #===========================================================================
    def generate_random_sources_from_image(self, step, black_value):
        '''Read pixel values from an image and according to the grey value in every pixel, create random 
        points. The size is adjustable with 'step' and the amount of points in black with 'black_value'.'''

        random_points = []

        for x in range(int(self.width / float(step))):
            for y in range(int(self.height / float(step))): 
                grey = self.get_color_grey(x*step, y*step)
                amount = int(map_range(grey, 0, 255, black_value, 0))
                for i in range(amount):
                    rndx = x*step + rnd.uniform(-1, 1)*step
                    rndy = y*step + rnd.uniform(-1, 1)*step
                    random_points.append(np.array([rndx, rndy, 0]))
        
        random_points = np.array(random_points)
        return random_points
    
    #===========================================================================
    def generate_init_nodes_from_image(self, num_init_nodes, thresh_nodes):  
        
        self.init_node_idxs = []
        
        # dart-throwing algorithm
        for i in range(num_init_nodes * 10):  
            tx = math.floor(rnd.random() * self.width)
            ty = math.floor(rnd.random() * self.height)
            
            grey = self.get_color_grey(tx, ty)
            if grey < thresh_nodes:
                position = np.array([tx, ty, 0])
                node = Node(position)
                self.nodes.append(node)
                self.init_node_idxs.append(len(self.nodes) - 1)
                
            if len(self.nodes) == num_init_nodes:
                break
    
    #===========================================================================
    def map_value_from_position(self,position):
        x, y, z = position
        value = self.get_color_grey(x, y)
        kill_distance = map_range(value, 0, 255, KILL_DISTANCE_MIN, KILL_DISTANCE_MAX)
        node_size = map_range(value, 0, 255, NODE_SIZE_MIN, NODE_SIZE_MAX)
        radius = map_range(value, 0, 255, RADIUS_MIN, RADIUS_MAX)
        step_size = map_range(value, 0, 255, STEP_SIZE_MIN, STEP_SIZE_MAX)
        return kill_distance, node_size, radius, step_size
    
    #===========================================================================
    def kill_sources_and_get_sources_within_radius(self, node):
        
        distances = np.linalg.norm(self.sources - node.position, axis = 1)
        idx_sorted = np.argsort(distances)
        distances_sorted = distances[idx_sorted]
        
        source_idxs_to_kill_sorted = np.where(distances_sorted < node.kill_distance)[0]        
        source_idxs_within_radius_sorted = np.where((distances_sorted >= node.kill_distance) & (distances_sorted <= node.radius))[0]
        
        #print "source_idxs_to_kill_sorted", source_idxs_to_kill_sorted
        #print "source_idxs_within_radius_sorted", source_idxs_within_radius_sorted
        
        source_idxs_to_kill = idx_sorted[source_idxs_to_kill_sorted]
        source_idxs_within_radius = idx_sorted[source_idxs_within_radius_sorted]
        
        #print "source_idxs_to_kill", source_idxs_to_kill
        #print "source_idxs_within_radius", source_idxs_within_radius
        
        sources_within_radius = np.array(self.sources)[source_idxs_within_radius]
        
        #print "sources_within_radius", sources_within_radius
        
        self.sources = np.delete(self.sources, source_idxs_to_kill, axis=0)
        
        return sources_within_radius
        
    #===========================================================================
    def get_closest_node_idx_to_source(self, node_positions, source):
        distances_squared = ((node_positions - source)**2).sum(axis=1)
        idx = np.argmin(distances_squared)
        return idx    
    #===========================================================================  
    def step(self):
         
        self.active_nodes = [node for node in self.nodes if node.active == True]
        max_children = max([node.num_children for node in self.nodes])
        
        node_positions = [node.position for node in self.active_nodes]
        
        # 1. assign sources to each node 
        for i, node in enumerate(self.active_nodes):
            node.sources = [] # delete everything to reassign
            if max_children > 0:
                # adjust the node size according to the amount of their children
                node.node_size = map_range(node.num_children, 0, max_children, NODE_SIZE_MIN, NODE_SIZE_MAX)    
             
            # kill the sources which are too close and assign sources to the node
            sources = self.kill_sources_and_get_sources_within_radius(node)
            
            # these sources must uniquely belong to one node, so we just add the ones which belong to node
            node_idxs = [self.get_closest_node_idx_to_source(node_positions, source) for source in sources]
            node_idxs_unique = [j for j, idx in enumerate(node_idxs) if idx == i]
            #node_idxs_unique = np.where(node_idxs == i)[0] # why is this not working ??

            node.sources = sources[node_idxs_unique]
             
            # set n.active False if no sources can be assigned
            if not len(node.sources):
                node.active = False
             
        
        self.active_nodes = [node for node in self.nodes if node.active == True]
        
        # 2. calculate for each active node the average direction where to put the next node
        del(self.new_nodes[:])

        for node in self.active_nodes:
            
            directions = np.array(node.sources) - node.position
            average_direction = np.sum(directions, axis=0)
            average_direction = average_direction/(np.linalg.norm(average_direction) * len(node.sources))
            node.direction = average_direction
            
            new_position = node.position + node.direction * node.step_size
            x, y, z = new_position
             
            if not (0 <= x < self.width and 0 <= y < self.height):
                node.active = False
                continue
            
            # add new node at the right place
            new_node = Node(new_position)
            kill_distance, node_size, radius, step_size = self.map_value_from_position(new_position)
            new_node.kill_distance = kill_distance
            #new_node.node_size = node_size
            new_node.radius = radius
            new_node.step_size = step_size
            new_node.parent = node
            self.add_child_to_all_parents(node)
            
            node.children.append(new_node)
            
            self.new_nodes.append(new_node)
        
        self.nodes += self.new_nodes
        
        print "len(self.nodes)", len(self.nodes)
        print "len(self.active_nodes)", len(self.active_nodes)
        print "len(self.sources)", len(self.sources)
         
    #===========================================================================
    def add_child_to_all_parents(self, node):
         
        def add_child_to_parent(node):
            if node.parent:
                node.parent.num_children += 1
                return True
            else:
                return False
             
        while add_child_to_parent(node):
            node = node.parent
    
    def get_paths(self):
        
        def recall(node, positions, paths):
            for i, child in enumerate(node.children):
                # po, pa = recall(child, [child.position], [])
                po, pa = recall(child, [node.position, child.position], []) # add also parent !
                if i == 0:
                    positions += po
                else:
                    if len(po): paths.append(po)
                paths += pa
            return positions, paths
        
        
        all_paths = []
        
        for idx in self.init_node_idxs:
            node = self.nodes[idx]
            positions, paths = recall(node, [node.position], [])
            all_paths += paths
            all_paths += [positions]
        return all_paths
            
            
            
if __name__ == "__main__":
    
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    import os
    
    
    step, black_value = 10, 30
    thresh_nodes = 180
    num_init_nodes = 20
    
    path = os.path.dirname(__file__)
    mas_lib_idx = path.find("mas_lib")
    mas_lib_path = path[:(mas_lib_idx + len("mas_lib"))]
    
    image_file = "algorithms\\dendrite_system\\food\\deer.jpg"
    image_file = os.path.join(mas_lib_path, image_file)

    ds = DendriteSystemFromImage(image_file, step, black_value, num_init_nodes, thresh_nodes)
    
    # draw
    fig, ax = plt.subplots()
    plt.axis('scaled') # keep aspect ratio
    ax.set_xlim(0, ds.width)
    ax.set_ylim(0, ds.height)
    
    max_iteration = 100
    
    def run(i):
        print "%i -------------------------" % i
        ds.step()
        
        node_positions = np.array([node.position for node in ds.nodes])
        xdata = node_positions[:,0]
        ydata = node_positions[:,1]
    
        if i == (max_iteration - 1):
            paths = ds.get_paths()
            print "len(paths)", len(paths)
            print sum([len(path) for path in paths])
            for path in paths:
                path = np.array(path)
                xdata = path[:,0]
                ydata = path[:,1]
                ax.plot(xdata, ydata)
        else:
            ax.plot(xdata, ydata, "o", markersize=1)
    

    ani = animation.FuncAnimation(fig, run, blit=False, frames=max_iteration, interval=10, repeat=False)
    plt.show()
    
    
    
    
    