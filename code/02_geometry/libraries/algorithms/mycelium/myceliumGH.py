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

Created on 04.10.2016

@author: kathrind

http://www.creativeapplications.net/processing/mycelium-processing/

'''

import math
import random as rnd
import ghpythonlib.components as ghcomp
import Rhino.Geometry as rg
from libraries.useful import clamp, map_range
from libraries.useful.color import convert_rgb_to_grey


#===============================================================================
class MyceliumGH:
    
    def __init__(self, image_file, number_of_worms, scale_factor = 1, speed = 10, branch_thresh = 1000, max_worms = 100, thresh_worm = 30, favour="light"):
        
        self.load_image(image_file)
        self.scale(scale_factor)
        
        self.max_worms = max_worms # maximum number of worms
     
        # controls when a worm will branch
        self.branch_thresh = branch_thresh
        self.thresh_worm = thresh_worm
        self.speed = speed
        
        self.init_worms(number_of_worms)
        
        self.dead_worms = []
        self.just_branched = 0
        self.favour = favour
        
        self.looking_angle = math.pi/12
        
    def load_image(self, image_file):
        self.cmesh = ghcomp.ImportImage(image_file)
        bb = self.cmesh.GetBoundingBox(rg.Plane.WorldXY)
        self.width = bb.Max.X
        self.height = bb.Max.Y
        self.point_cloud = rg.PointCloud(self.cmesh.Vertices.ToPoint3dArray())
    
    def get_grey_value(self, x, y):
        point = rg.Point3d(x, y, 0)
        color_rgb = self.cmesh.VertexColors[self.point_cloud.ClosestPoint(point)]
        grey = convert_rgb_to_grey(color_rgb.R, color_rgb.G, color_rgb.B)
        grey = clamp(grey, 0, 255)
        return grey
    
    def get_score_from_grey_value(self, x, y):
        grey = self.get_grey_value(x,y)
        ts = 4 * grey
        return {'grey': grey, 'score': ts}
    
    def scale(self, factor):
        S = rg.Transform.Scale(rg.Plane.WorldXY, factor, factor, factor)
        self.cmesh.Transform(S)
        self.point_cloud.Transform(S)
        self.width *= factor
        self.height *= factor
     
    def init_worms(self, number_of_worms):
        
        self.worms = []
        
        """
        for i in range(number_of_worms):
            tx = math.floor(rnd.random() * self.width)
            ty = math.floor(rnd.random() * self.height)
            angle = rnd.random() * 2 * math.pi
            worm = Worm(tx, ty, angle, self)
            worms.append(worm)
        """
        
        # only init worms on dark spots of the image
        for i in range(number_of_worms * 10):
            
            tx = math.floor(rnd.random() * self.width)
            ty = math.floor(rnd.random() * self.height)
            angle = rnd.random() * 2 * math.pi
            
            grey = self.get_grey_value(tx, ty)
            if grey < self.thresh_worm:
                self.add_worm(tx, ty, angle)
            if len(self.worms) == number_of_worms:
                break
    
    def add_worm(self, tx, ty, angle, index=None):
        if index:
            self.worms[index] = WormGH(tx, ty, angle, self)
        else:
            self.worms.append(WormGH(tx, ty, angle, self))
    
    def step(self):
        #print self.worms
        for i, w in enumerate(self.worms):
            if not w.dead:

                # save the worms points for the worm path      
                w.points.append((w.x,w.y))
                 
                # move all the worms
                w.x += (math.cos(w.angle) * self.speed)
                w.y += (math.sin(w.angle) * self.speed)
     
                w.update_direction()
     
                
                if (w.x > self.width) or (w.x < 0) or (w.y > self.height) or (w.y < 0):
                    w.points.append(())
                
                # Wrap the worms around the canvas 
                if w.x > self.width: w.x = 0
                if w.x < 0: w.x = self.width
                if w.y > self.height: w.y = 0
                if w.y < 0: w.y = self.height
                
            else:
                # regenerate an available worm at a random slot
                grey = 255
                while grey > self.thresh_worm:            
                    tx = math.floor(rnd.random() * self.width)
                    ty = math.floor(rnd.random() * self.height)
         
                    # assign a random vector to begin with
                    angle = rnd.random() * 2 * math.pi
                     
                    grey = self.get_grey_value(tx, ty)
                    self.dead_worms.append(self.worms[i])  
                    self.add_worm(tx, ty, angle, i)
        
            # draw geometry
            if len(w.points) > 2:
                if(len(w.points[-2]) and len(w.points[-1])):
                    x1, y1 = w.points[-2]
                    x2, y2 = w.points[-1]
                    w.add_geometry(rg.Line(rg.Point3d(x1, y1, 0), rg.Point3d(x2, y2, 0)))


         
#===============================================================================
class WormGH:
     
    def __init__(self, x, y, angle, parent):
        self.x = x
        self.y = y
        self.angle = angle
        self.food = 100
        self.dead = False
        self.grey = 0
        self.points = []
        self.parent = parent
        
        self.geometry = []
    
    def add_geometry(self, geo):
        self.geometry.append(geo)
    
    def get_polylines(self):
        
        polylines = []
        polyline_pts = []
        
        for p in self.points:
            if list(p) == []:
                # make a new polyline
                polylines.append(rg.PolylineCurve(polyline_pts))
                polyline_pts = []
            else:
                x, y = p
                polyline_pts.append(rg.Point3d(x, y, 0))
        polylines.append(rg.PolylineCurve(polyline_pts))
        
        return polylines
            
        
    def update_direction(self):
                
        # we know the current location, we know the vector
        # calculate a few variations between -30 degrees and +30 degree and get their colors
        # whichever is brightest, that's where we go to. 
         
        angle = 0
        best_angle = 0
        best_score_so_far = {'grey': 0, 'angle': 0, 'score': 99999999 }
     
        # look for the best place to go
        for i in range(12):
     
            angle = self.angle - ((rnd.random() * self.parent.looking_angle)) + ((rnd.random() * self.parent.looking_angle))
            
            # calculate a new direction                
            tx = self.x + (math.cos(angle) * self.parent.speed)
            ty = self.y + (math.sin(angle) * self.parent.speed) # 5 makes it look further out
     
            # test the source image
            score = self.parent.get_score_from_grey_value(tx, ty)
     
            # swap > for < 
            if (score['score'] < best_score_so_far['score']):
                best_angle = angle
                score['angle'] = angle
                best_score_so_far = score        
     
        self.parent.just_branched -= 1
     
        # If the score is SOO good, we should branch (unless maximum worms have been reached
        if (best_score_so_far['score'] > self.parent.branch_thresh):
     
            if (self.parent.just_branched <= 0):
                # assign a new vector, close to the original
                start_angle = self.angle + ((rnd.random() * self.parent.looking_angle))
                self.angle -= 0.37
     
                if (len(self.parent.worms) < self.parent.max_worms):
                    # new worm

                    self.parent.add_worm(self.x, self.y, start_angle)
                    
                    # we don't want everything branching at once
                    self.parent.just_branched = 500
                
                   
                else:
                    # maybe we can find a dead-worm and re-use him
                    for i, w in enumerate(self.parent.worms):
                        if w.dead == True:
                            self.parent.add_worm(self.x, self.y, start_angle, i)
                            break
     
        self.angle = best_angle
        self.food -= 1
     
        if self.parent.favour == "light": # favor the light
            if best_score_so_far['score'] > 755:
                self.food = 200
        else: # favor the dark
            if best_score_so_far['score'] < 355:
                self.food = 200
     
        if self.food == 0:
            self.dead = True
 

#===============================================================================